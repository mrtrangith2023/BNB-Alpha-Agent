from fastapi import FastAPI

app = FastAPI(
    title="BNB Alpha Agent",
    description="Autonomous Trading Agent",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "project": "BNB Alpha Agent",
        "status": "running"
    }

@app.get("/market")
def market():
    return {
        "signal": "BUY",
        "confidence": 82
    }

@app.get("/risk")
def risk():
    return {
        "risk_score": 25,
        "level": "LOW"
    }

@app.get("/portfolio")
def portfolio():
    return {
        "status": "monitoring",
        "positions": 2
    }