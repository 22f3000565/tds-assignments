from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import numpy as np
import json
import pathlib

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"]
)

DATA_FILE = pathlib.Path(__file__).parent / "q-vercel-latency.json"
with open(DATA_FILE, "r") as f:
    telemetry = json.load(f)

@app.options("/")
async def options_root():
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
    }
    return JSONResponse(status_code=204, content=None, headers=headers)

@app.post("/")
async def get_metrics(req: Request):
    body = await req.json()
    regions = body.get("regions", [])
    threshold = body.get("threshold_ms", 180)

    response_regions = []

    for region in regions:
        records = [r for r in telemetry if r["region"] == region]
        if not records:
            continue

        latencies = [r["latency_ms"] for r in records]
        uptimes = [r["uptime_pct"] for r in records]

        avg_latency = round(float(np.mean(latencies)), 2)
        p95_latency = round(float(np.percentile(latencies, 95)), 2)
        avg_uptime = round(float(np.mean(uptimes)), 3)
        breaches = sum(1 for l in latencies if l > threshold)

        response_regions.append({
            "region": region,
            "avg_latency": avg_latency,
            "p95_latency": p95_latency,
            "avg_uptime": avg_uptime,
            "breaches": breaches
        })

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
    }

    return JSONResponse(content={"regions": response_regions}, headers=headers)
