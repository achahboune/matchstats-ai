from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from .provider import fetch_matches
from .analysis import summarize_match

app = FastAPI(title="MatchStats AI", version="1.0.0",
              description="Football match insights, summaries and baseline probability estimates.")
BASE_DIR = Path(__file__).resolve().parent.parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

@app.get("/", include_in_schema=False)
async def home():
    return FileResponse(BASE_DIR / "static" / "index.html")

@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "MatchStats AI"}

@app.get("/api/matches")
async def matches():
    data, source = await fetch_matches()
    return {"source": source, "count": len(data), "matches": data}

@app.get("/api/matches/{match_id}")
async def match_detail(match_id: int):
    data, source = await fetch_matches()
    match = next((m for m in data if m.get("id") == match_id), None)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return {"source": source, "match": match}

@app.get("/api/matches/{match_id}/analysis")
async def match_analysis(match_id: int):
    data, source = await fetch_matches()
    match = next((m for m in data if m.get("id") == match_id), None)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return {"source": source, "analysis": summarize_match(match)}
