import os
import httpx
from .data import DEMO_MATCHES

BASE_URL = os.getenv("API_FOOTBALL_BASE_URL", "https://v3.football.api-sports.io")
API_KEY = os.getenv("API_FOOTBALL_KEY", "").strip()

async def fetch_matches():
    """Return provider fixtures when configured; otherwise return demo fixtures."""
    if not API_KEY:
        return DEMO_MATCHES, "demo"
    headers = {"x-apisports-key": API_KEY}
    params = {"live": "all"}
    try:
        async with httpx.AsyncClient(timeout=12) as client:
            response = await client.get(f"{BASE_URL}/fixtures", headers=headers, params=params)
            response.raise_for_status()
            payload = response.json()
        fixtures = payload.get("response", [])
        return [normalize_fixture(item) for item in fixtures], "api-football"
    except (httpx.HTTPError, ValueError, KeyError):
        # Keep the UI available during provider outages or quota exhaustion.
        return DEMO_MATCHES, "demo-fallback"

def normalize_fixture(item):
    fixture = item.get("fixture", {})
    league = item.get("league", {})
    teams = item.get("teams", {})
    goals = item.get("goals", {})
    status = fixture.get("status", {})
    return {
        "id": fixture.get("id"),
        "league": league.get("name", "Unknown league"),
        "country": league.get("country", ""),
        "date": fixture.get("date"),
        "status": status.get("short", "NS"),
        "status_long": status.get("long", "Not Started"),
        "elapsed": status.get("elapsed"),
        "home": teams.get("home", {}),
        "away": teams.get("away", {}),
        "goals": goals,
        "venue": (fixture.get("venue") or {}).get("name", ""),
    }
