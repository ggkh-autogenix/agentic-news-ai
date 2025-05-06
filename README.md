# Agentic News AI 🧠📰

An agentic AI system that autonomously fetches, summarizes, and sends real-time news updates via WhatsApp.

## Features
- Fetches real-time news via NewsAPI
- Summarizes articles using OpenAI (LangChain)
- Sends updates using Twilio WhatsApp API
- Modular agentic workflow using LangGraph

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Endpoint

- `POST /daily-summary` with JSON `{"topic": "technology"}`

## Environment Variables

Configure `.env`:
```
OPENAI_API_KEY=
NEWSAPI_KEY=
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE=
TO_PHONE=
```