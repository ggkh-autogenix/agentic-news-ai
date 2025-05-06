from fastapi import FastAPI, Request
from scraper import scrape_articles
from summarizer import summarize_articles
from whatsapp import send_whatsapp
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()

@app.post("/daily-summary")
async def daily_summary(request: Request):
    data = await request.json()
    urls = data.get("urls", [])
    phone = data.get("phone", "")

    articles = scrape_articles(urls)
    summary = summarize_articles(articles)
    send_whatsapp(phone, summary)
    return {"status": "Summary sent"}

scheduler = BackgroundScheduler()
scheduler.start()
