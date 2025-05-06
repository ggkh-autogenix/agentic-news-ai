


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


