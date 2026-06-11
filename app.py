from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "BNB Alpha Agent",
        "status": "active"
    }