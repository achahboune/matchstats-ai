# MatchStats AI

A football match intelligence dashboard with live-score integration, team statistics, AI-style match summaries, and transparent probability estimates.

## Features
- Match dashboard with live and upcoming fixtures
- Match details: score, status, events, team statistics
- Automated match summaries
- Explainable win/draw/loss estimates (heuristic baseline, not betting advice)
- REST API built with FastAPI
- Works in demo mode without an API key
- Optional API-Football integration for real fixtures

## Quick start (Python 3.10+)

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000

## Live data
The app runs with sample fixtures by default. To enable API-Football:
1. Get an API key from https://www.api-football.com/
2. Set `API_FOOTBALL_KEY` in your environment.
3. Optionally set `API_FOOTBALL_BASE_URL` (default: `https://v3.football.api-sports.io`).

PowerShell:
```powershell
$env:API_FOOTBALL_KEY="your_key"
uvicorn app.main:app --reload
```

The provider's plan, rate limits, coverage, and licensing apply. Do not redistribute provider data unless your plan permits it.

## API
- `GET /api/health`
- `GET /api/matches`
- `GET /api/matches/{match_id}`
- `GET /api/matches/{match_id}/analysis`

Interactive API docs: http://127.0.0.1:8000/docs

## Docker

```bash
docker compose up --build
```

## Project structure
```text
app/
  main.py
  data.py
  provider.py
  analysis.py
static/
  index.html
  styles.css
  app.js
tests/
  test_analysis.py
Dockerfile
docker-compose.yml
requirements.txt
```

## Important
Predictions are illustrative statistical estimates generated from limited inputs. They are not guaranteed outcomes and must not be used as the sole basis for betting or financial decisions.
