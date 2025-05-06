Here's a **clean, simple Agentic AI PoC** version of your project to include in a GitHub repo and send to investors. It includes:

* ✅ Clear structure
* ✅ Uses FastAPI for endpoints
* ✅ Dynamically accepts newspaper URLs and API keys
* ✅ Sends short WhatsApp summaries
* ✅ Includes `README.md` content ready to copy-paste

---

### 🗂️ **Project Structure**

```
agentic-news-ai/
├── main.py
├── summarizer.py
├── scraper.py
├── messenger.py
├── requirements.txt
└── README.md
```

---

### 📄 `main.py`

```python
from fastapi import FastAPI, Request
from scraper import scrape_articles
from summarizer import summarize_articles
from messenger import send_whatsapp

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Agentic News AI!"}

@app.post("/daily-summary")
async def daily_summary(request: Request):
    data = await request.json()
    urls = data.get("urls", [])
    phone = data.get("phone", "")
    openai_key = data.get("openai_key", "")

    if not urls or not phone or not openai_key:
        return {"error": "Missing urls, phone or API key"}

    articles = scrape_articles(urls)
    summary = summarize_articles(articles, openai_key)
    send_whatsapp(phone, summary)
    return {"status": "Summary sent", "summary": summary}
```

---

### 📄 `scraper.py`

```python
import requests
from bs4 import BeautifulSoup

def scrape_articles(urls):
    articles = []
    for url in urls:
        try:
            html = requests.get(url, timeout=10).text
            soup = BeautifulSoup(html, 'html.parser')
            paragraphs = soup.find_all('p')
            text = ' '.join(p.get_text() for p in paragraphs[:10])
            articles.append({"url": url, "text": text})
        except Exception:
            continue
    return articles
```

---

### 📄 `summarizer.py`

```python
import requests

def summarize_articles(articles, user_api_key):
    text_input = "\n\n".join([a["text"][:500] for a in articles])
    prompt = (
        "Summarize the following news in under 100 words. "
        "Group by category: Politics, Economy, Sports, Technology, World. "
        "Avoid repetition, focus on key facts:\n\n" + text_input
    )

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {user_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    return result['choices'][0]['message']['content']
```

---

### 📄 `messenger.py`

```python
from twilio.rest import Client
import os

def send_whatsapp(to, message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_whatsapp_number = os.getenv("TWILIO_FROM_WHATSAPP")

    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=f'whatsapp:{from_whatsapp_number}',
        to=f'whatsapp:{to}'
    )
```

---

### 📄 `requirements.txt`

```
fastapi
uvicorn
requests
beautifulsoup4
twilio
```

---

### 📄 `README.md`

````markdown
# Agentic News AI 📰🤖

A simple Proof of Concept Agentic AI that:
- Reads news articles from user-submitted URLs
- Uses OpenRouter AI to summarize content under 100 words
- Categorizes by topic (Politics, Economy, Sports, Tech, World)
- Sends the final summary via WhatsApp

## 🚀 Features
- Dynamic article input
- Uses user’s OpenAI-compatible API key
- Designed for low-cost deployment (OpenRouter + FastAPI)
- Lightweight, investor-friendly PoC

## 📦 Requirements
- Python 3.11+
- Twilio account for WhatsApp API (free tier supported)
- OpenRouter/OpenAI API Key

## 🛠️ Setup

```bash
pip install -r requirements.txt
````

Set environment variables for Twilio:

```bash
export TWILIO_ACCOUNT_SID=your_sid
export TWILIO_AUTH_TOKEN=your_token
export TWILIO_FROM_WHATSAPP=whatsapp:+14155238886
```

Run the server:

```bash
uvicorn main:app --reload
```

## 🧪 Test with Postman

POST `/daily-summary`

```json
{
  "urls": [
    "https://www.bbc.com/news/world",
    "https://www.cnn.com/2024/11/10/politics/us-election.html"
  ],
  "phone": "+911234567890",
  "openai_key": "sk-xxxxxxxxxxxxxxxxxxxxxx"
}
```

## 📩 Output

Summarized news sent to your WhatsApp in <100 words per day.

## 🧠 Built With

* [FastAPI](https://fastapi.tiangolo.com/)
* [OpenRouter](https://openrouter.ai/)
* [Twilio](https://www.twilio.com/whatsapp)

```

---

### ✅ Next Steps
- Push this to GitHub.
- Deploy to [Render](https://render.com/) or [Railway](https://railway.app/).
- Share public API link + sample Postman collection with investors.

Would you like me to generate the GitHub repo structure or a ZIP you can upload directly?
```
