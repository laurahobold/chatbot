# Chatbot (AgentOS + OpenAI)

A compact experimental chatbot combining AgentOS with OpenAI. Intended for quick local development: a FastAPI backend and a Next.js frontend (AgentUI).

What's here
- backend/ — FastAPI + AgentOS (no DB required by default)
- frontend/agent-ui — Next.js UI
- docker-compose.yml — containerized setup

## Quick start — Docker (recommended)
1. Set your environment variables in a `.env` file (see `.env.example`):
   - `OPENAI_API_KEY=sk-...your-key...`
2. From project root, run:
```cmd
docker-compose up --build
```
- Backend will be at http://localhost:7777
- Frontend UI at http://localhost:3000

## Manual setup — backend
1. Create & activate venv:
```cmd
python -m venv .venv
.venv\Scripts\activate
```
2. Install deps and set your OpenAI key:
```cmd
pip install -r backend/requirements.txt
set OPENAI_API_KEY=sk-...your-key...
```
3. Run backend:
```cmd
cd backend
uvicorn app:app --reload --port 8000
```

## Manual setup — frontend
```cmd
cd frontend\agent-ui
npm install
npm run dev
```
Open http://localhost:3000 (frontend) and ensure backend is at http://localhost:8000.

## Environment
- `OPENAI_API_KEY` — required

## Troubleshooting
- OpenAI errors: verify `OPENAI_API_KEY` and network access.
- Connection/CORS: confirm backend is running on port 8000 or 7777 (Docker).

## Notes
- Profile/memory persistence is a work in progress.
- If you enable DB persistence later, set `DATABASE_URL` and update backend config.
