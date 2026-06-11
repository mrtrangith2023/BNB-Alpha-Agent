from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"project": "BNB Alpha Agent"}

@app.get("/market")
def market():
    return {"signal": "BUY"}

@app.get("/risk")
def risk():
    return {"risk_score": 25}

@app.get("/portfolio")
def portfolio():
    return {"status": "monitoring"}