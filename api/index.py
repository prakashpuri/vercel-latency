from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA = [
  {"region":"apac","latency_ms":216.44,"uptime_pct":98.039},
  {"region":"apac","latency_ms":138.52,"uptime_pct":99.076},
  {"region":"apac","latency_ms":188.19,"uptime_pct":98.619},
  {"region":"apac","latency_ms":142.06,"uptime_pct":98.132},
  {"region":"apac","latency_ms":212.05,"uptime_pct":99.016},
  {"region":"apac","latency_ms":128.71,"uptime_pct":97.61},
  {"region":"apac","latency_ms":217.06,"uptime_pct":99.285},
  {"region":"apac","latency_ms":130.98,"uptime_pct":97.243},
  {"region":"apac","latency_ms":105.58,"uptime_pct":98.725},
  {"region":"apac","latency_ms":145.2,"uptime_pct":98.413},
  {"region":"apac","latency_ms":208.78,"uptime_pct":97.898},
  {"region":"apac","latency_ms":131.1,"uptime_pct":98.299},
  {"region":"emea","latency_ms":222.1,"uptime_pct":99.132},
  {"region":"emea","latency_ms":219.35,"uptime_pct":97.797},
  {"region":"emea","latency_ms":128.73,"uptime_pct":98.117},
  {"region":"emea","latency_ms":147.93,"uptime_pct":98.236},
  {"region":"emea","latency_ms":223.47,"uptime_pct":98.46},
  {"region":"emea","latency_ms":124.02,"uptime_pct":99.443},
  {"region":"emea","latency_ms":173.75,"uptime_pct":98.036},
  {"region":"emea","latency_ms":189.53,"uptime_pct":98.807},
  {"region":"emea","latency_ms":177.74,"uptime_pct":97.135},
  {"region":"emea","latency_ms":179.56,"uptime_pct":98.622},
  {"region":"emea","latency_ms":193.94,"uptime_pct":97.172},
  {"region":"emea","latency_ms":127.6,"uptime_pct":97.662},
  {"region":"amer","latency_ms":182.72,"uptime_pct":99.282},
  {"region":"amer","latency_ms":171.96,"uptime_pct":97.518},
  {"region":"amer","latency_ms":211.08,"uptime_pct":98.953},
  {"region":"amer","latency_ms":147.98,"uptime_pct":99.072},
  {"region":"amer","latency_ms":150.0,"uptime_pct":98.544},
  {"region":"amer","latency_ms":125.02,"uptime_pct":98.2},
  {"region":"amer","latency_ms":234.56,"uptime_pct":98.644},
  {"region":"amer","latency_ms":189.51,"uptime_pct":97.762},
  {"region":"amer","latency_ms":160.11,"uptime_pct":97.829},
  {"region":"amer","latency_ms":186.12,"uptime_pct":99.189},
  {"region":"amer","latency_ms":137.51,"uptime_pct":98.758},
  {"region":"amer","latency_ms":214.3,"uptime_pct":98.61},
]

def mean(lst):
    return sum(lst) / len(lst)

def percentile(lst, p):
    sorted_lst = sorted(lst)
    k = (len(sorted_lst) - 1) * p / 100
    f = int(k)
    c = f + 1
    if c >= len(sorted_lst):
        return sorted_lst[f]
    return sorted_lst[f] + (k - f) * (sorted_lst[c] - sorted_lst[f])

class RequestBody(BaseModel):
    regions: List[str]
    threshold_ms: float

@app.post("/api")
def get_metrics(body: RequestBody):
    result = {}
    for region in body.regions:
        records = [d for d in DATA if d["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes = [r["uptime_pct"] for r in records]
        result[region] = {
            "avg_latency": round(mean(latencies), 4),
            "p95_latency": round(percentile(latencies, 95), 4),
            "avg_uptime": round(mean(uptimes), 4),
            "breaches": sum(1 for l in latencies if l > body.threshold_ms)
        }
    return result
