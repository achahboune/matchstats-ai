from datetime import datetime, timedelta, timezone

NOW = datetime.now(timezone.utc)

DEMO_MATCHES = [
    {
        "id": 1001, "league": "Premier League", "country": "England",
        "date": (NOW + timedelta(minutes=35)).isoformat(),
        "status": "NS", "status_long": "Not Started", "elapsed": None,
        "home": {"id": 42, "name": "Arsenal", "logo": ""},
        "away": {"id": 50, "name": "Manchester City", "logo": ""},
        "goals": {"home": None, "away": None},
        "venue": "Emirates Stadium",
    },
    {
        "id": 1002, "league": "La Liga", "country": "Spain",
        "date": (NOW - timedelta(minutes=22)).isoformat(),
        "status": "2H", "status_long": "Second Half", "elapsed": 67,
        "home": {"id": 529, "name": "Barcelona", "logo": ""},
        "away": {"id": 541, "name": "Real Madrid", "logo": ""},
        "goals": {"home": 2, "away": 1},
        "venue": "Estadi Olímpic Lluís Companys",
    },
    {
        "id": 1003, "league": "Serie A", "country": "Italy",
        "date": (NOW + timedelta(hours=2)).isoformat(),
        "status": "NS", "status_long": "Not Started", "elapsed": None,
        "home": {"id": 489, "name": "AC Milan", "logo": ""},
        "away": {"id": 496, "name": "Inter", "logo": ""},
        "goals": {"home": None, "away": None},
        "venue": "San Siro",
    },
    {
        "id": 1004, "league": "Bundesliga", "country": "Germany",
        "date": (NOW - timedelta(hours=2)).isoformat(),
        "status": "FT", "status_long": "Match Finished", "elapsed": 90,
        "home": {"id": 157, "name": "Bayern Munich", "logo": ""},
        "away": {"id": 165, "name": "Borussia Dortmund", "logo": ""},
        "goals": {"home": 3, "away": 1},
        "venue": "Allianz Arena",
    },
]
