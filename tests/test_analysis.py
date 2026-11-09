from app.analysis import estimate_probabilities, summarize_match

def test_probabilities_sum_to_100():
    result = estimate_probabilities()
    assert round(result["home_win"] + result["draw"] + result["away_win"], 1) == 100.0

def test_summary_for_finished_match():
    match = {
        "home": {"name": "Home FC"}, "away": {"name": "Away FC"},
        "goals": {"home": 2, "away": 0}, "status": "FT",
        "status_long": "Match Finished",
    }
    result = summarize_match(match)
    assert "Home FC won 2-0" in result["summary"]
