from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA = [
  {"region":"apac","service":"analytics","latency_ms":216.44,"uptime_pct":98.039},
  {"region":"apac","service":"analytics","latency_ms":138.52,"uptime_pct":99.076},
  {"region":"apac","service":"analytics","latency_ms":188.19,"uptime_pct":98.619},
  {"region":"apac","service":"catalog","latency_ms":142.06,"uptime_pct":98.132},
  {"region":"apac","service":"checkout","latency_ms":212.05,"uptime_pct":99.016},
  {"region":"apac","service":"payments","latency_ms":128.71,"uptime_pct":97.61},
  {"region":"apac","service":"analytics","latency_ms":217.06,"uptime_pct":99.285},
  {"region":"apac","service":"checkout","latency_ms":130.98,"uptime_pct":97.243},
  {"region":"apac","service":"support","latency_ms":105.58,"uptime_pct":98.725},
  {"region":"apac","service":"catalog","latency_ms":145.2,"uptime_pct":98.413},
  {"region":"apac","service":"support","latency_ms":208.78,"uptime_pct":97.898},
  {"region":"apac","service":"recommendations","latency_ms":131.1,"uptime_pct":98.299},
  {"region":"emea","service":"support","latency_ms":222.1,"uptime_pct":99.132},
  {"region":"emea","service":"analytics","latency_ms":219.35,"uptime_pct":97.797},
  {"region":"emea","service":"analytics","latency_ms":128.73,"uptime_pct":98.117},
  {"region":"emea","service":"recommendations","latency_ms":147.93,"uptime_pct":98.236},
  {"region":"emea","service":"analytics","latency_ms":223.47,"uptime_pct":98.46},
  {"region":"emea","service":"analytics","latency_ms":124.02,"uptime_pct":99.443},
  {"region":"emea","service":"checkout","latency_ms":173.75,"uptime_pct":98.036},
  {"region":"emea","service":"payments","latency_ms":189.53,"uptime_pct":98.807},
  {"
