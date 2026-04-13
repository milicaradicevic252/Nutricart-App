# Nutricart-App

AI-powered grocery assistant that analyzes food items, provides nutrition insights, and suggests healthier alternatives.

## Project Structure

- `backend/`: Flask API for food analysis endpoints.
- `frontend/`: Frontend scaffold for the NutriCart UI.

## Backend Quick Start

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

### Available API Routes

- `GET /` → returns `NutriCart API is running`
- `POST /analyze-food` with JSON body `{"item": "banana"}`
