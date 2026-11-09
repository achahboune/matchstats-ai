def estimate_probabilities(home_strength=1.55, away_strength=1.25):
    """A simple Poisson-inspired baseline; replace with trained data for production."""
    home = max(0.1, min(float(home_strength), 3.5))
    away = max(0.1, min(float(away_strength), 3.5))
    edge = (home - away) + 0.22  # small home advantage
    home_win = 1 / (1 + pow(2.71828, -1.45 * (edge - 0.18)))
    draw = max(0.16, 0.29 - abs(edge) * 0.055)
    away_win = max(0.05, 1 - home_win - draw)
    total = home_win + draw + away_win
    return {
        "home_win": round(home_win / total * 100, 1),
        "draw": round(draw / total * 100, 1),
        "away_win": round(away_win / total * 100, 1),
        "model": "baseline-heuristic",
    }

def summarize_match(match):
    home = match.get("home", {}).get("name", "Home")
    away = match.get("away", {}).get("name", "Away")
    goals = match.get("goals") or {}
    hg, ag = goals.get("home"), goals.get("away")
    status = match.get("status_long", "Scheduled")
    if hg is None or ag is None:
        probs = estimate_probabilities()
        leader = max((("home", probs["home_win"]), ("draw", probs["draw"]), ("away", probs["away_win"])), key=lambda x: x[1])[0]
        lean = {"home": home, "draw": "a draw", "away": away}[leader]
        return {
            "headline": f"{home} vs {away}",
            "summary": f"The fixture is {status.lower()}. The baseline model currently leans toward {lean}.",
            "score": None,
            "probabilities": probs,
            "caveat": "Estimate only: no confirmed lineups, injuries, or live event context are included.",
        }
    if hg > ag:
        result = f"{home} lead {hg}-{ag}" if match.get("status") != "FT" else f"{home} won {hg}-{ag}"
    elif ag > hg:
        result = f"{away} lead {ag}-{hg}" if match.get("status") != "FT" else f"{away} won {ag}-{hg}"
    else:
        result = f"The match is level at {hg}-{ag}"
    return {
        "headline": f"{home} {hg}–{ag} {away}",
        "summary": f"{result}. Match status: {status}.",
        "score": {"home": hg, "away": ag},
        "probabilities": None,
        "caveat": "Summary is generated from the score and status supplied by the data provider.",
    }
