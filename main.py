from fastapi import FastAPI, Request
from agentic_news_agent import run_agentic_news
from messenger import send_whatsapp

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Agentic News AI!"}

@app.post("/daily-summary")
async def daily_summary(request: Request):
    data = await request.json()
    topic = data.get("topic", "technology")
    summary = run_agentic_news(topic)
    send_whatsapp(summary)
    return {"message": "News summary sent via WhatsApp."}