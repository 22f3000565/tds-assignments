from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import json
import pathlib
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS for all origins and POST
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"],
)

# Load the telemetry data once (from bundled JSON file in project root)
DATA_FILE = pathlib.Path(__file__).parent.parent / "q-vercel-latency.json"
with open(DATA_FILE, "r") as f:
    telemetry = json.load(f)

# handle preflight manually
@app.options("/")
async def preflight(req: Request):
    return JSONResponse(status_code=200, content={})

@app.post("/")
async def get_metrics(req: Request):
    body = await req.json()
    regions = body.get("regions", [])
    threshold = body.get("threshold_ms", 180)

    result = {}

    for region in regions:
        # filter records for this region
        records = [r for r in telemetry if r["region"] == region]

        if not records:
            continue

        latencies = [r["latency_ms"] for r in records]
        uptimes = [r["uptime_pct"] for r in records]

        avg_latency = float(np.mean(latencies))
        p95_latency = float(np.percentile(latencies, 95))
        avg_uptime = float(np.mean(uptimes))
        breaches = sum(1 for l in latencies if l > threshold)

        result[region] = {
            "avg_latency": round(avg_latency, 2),
            "p95_latency": round(p95_latency, 2),
            "avg_uptime": round(avg_uptime, 3),
            "breaches": breaches,
        }

    return result
