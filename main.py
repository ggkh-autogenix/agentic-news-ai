from fastapi import FastAPI, Request
from scraper import scrape_articles
from summarizer import summarize_articles
from whatsapp import send_whatsapp
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to ggkh-agenticnews-ai"}
    
@app.post("/daily-summary")
async def daily_summary(request: Request):
    data = await request.json()
    urls = data.get("urls", [])
    phone = data.get("phone", "")
    user_api_key = data.get("openai_key", "")

    if not user_api_key:
        return {"error": "Missing OpenAI API key"}

    articles = scrape_articles(urls)
    summary = summarize_articles(articles, user_api_key)
    send_whatsapp(phone, summary)
    return {"status": "Summary sent"}

scheduler = BackgroundScheduler()
scheduler.start()
