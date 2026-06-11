# BNB Alpha Agent

Autonomous Trading Agent built on BNB Chain.

## Features

- Market Signal API
- Risk Management API
- Portfolio Monitoring API
- FastAPI Backend

## API Endpoints

GET /
GET /market
GET /risk
GET /portfolio

## Run

pip install -r requirements.txt

python -m uvicorn app:app --reload

## Architecture

FastAPI
→ Market Engine
→ Risk Engine
→ Portfolio Engine

## Roadmap

Phase 1
- Market monitoring

Phase 2
- AI signal generation

Phase 3
- Autonomous execution