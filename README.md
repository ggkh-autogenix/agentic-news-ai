Here's a complete and professional `README.md` file tailored for your **Agentic AI News Summarizer** project:

---

```markdown
# 📰 Agentic AI News Summarizer

This project is an **agentic AI-powered system** that reads news from multiple dynamically provided websites, summarizes key insights across categories like **Politics, Economy, Technology, Sports, and World**, and sends the final summary as a **WhatsApp message** to a dynamically specified phone number.

Ideal for keeping yourself and your network updated with a concise, daily, AI-curated news digest.

---

## 🌟 Features

- ✅ Scrapes real-time content from any newspaper website (URL provided via API).
- ✅ Uses OpenAI GPT-4 to summarize and categorize articles into high-level topics.
- ✅ Limits output to 50 lines max.
- ✅ Sends summary via WhatsApp using Twilio API.
- ✅ Accepts dynamic list of URLs and phone numbers.
- ✅ Can be scheduled as a daily task using Render cron jobs.

---

## 📦 Project Structure

```

agentic-news-ai/
├── main.py             # FastAPI web server
├── scraper.py          # News article extraction
├── summarizer.py       # GPT-powered summarization
├── whatsapp.py         # WhatsApp sending using Twilio
├── requirements.txt    # Python dependencies
├── render.yaml         # Render deployment config
├── .replit             # For optional Replit deployment
└── README.md           # Project documentation

````

---

## 🚀 Deployment Guide

### 🛠 Prerequisites

- Python 3.8+
- [OpenAI API Key](https://platform.openai.com/)
- [Twilio Account with WhatsApp](https://www.twilio.com/whatsapp)

### 1. Clone This Repo

```bash
git clone https://github.com/your-username/agentic-news-ai.git
cd agentic-news-ai
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables

Set the following environment variables in your system or via `.env` (or Render dashboard):

```bash
OPENAI_API_KEY=your_openai_key
TWILIO_SID=your_twilio_sid
TWILIO_TOKEN=your_twilio_token
TWILIO_WHATSAPP=whatsapp:+14155238886
```

---

## 🔄 API Usage

### `POST /daily-summary`

Sends a WhatsApp message with a summarized view of the given articles.

#### Request Body:

```json
{
  "urls": [
    "https://www.bbc.com/news",
    "https://edition.cnn.com"
  ],
  "phone": "+911234567890"
}
```

#### Response:

```json
{
  "status": "Summary sent"
}
```

---

## 📆 Scheduling Daily Summary (Render)

1. Go to your Render dashboard.
2. Create a new **Cron Job** (type: `POST`).
3. URL: `https://your-app-url.onrender.com/daily-summary`
4. Body:

   ```json
   {
     "urls": ["https://bbc.com/news", "https://cnn.com"],
     "phone": "+911234567890"
   }
   ```
5. Schedule: `0 8 * * *` for 8AM UTC daily.

---

## 🧪 Test Locally

```bash
uvicorn main:app --reload
```

Then test with a tool like [Postman](https://www.postman.com/) or curl:

```bash
curl -X POST http://127.0.0.1:8000/daily-summary \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://bbc.com/news"], "phone": "+911234567890"}'
```

---

## ✨ Credits

* GPT summarization: [OpenAI](https://openai.com/)
* WhatsApp messaging: [Twilio](https://www.twilio.com/whatsapp)
* News scraping: [newspaper3k](https://github.com/codelucas/newspaper)

---

## 📬 Contact

Built by **Easy Life Innovations**
For queries, reach out via GitHub issues or email.

```

---

Let me know if you want this customized with your company name or GitHub username pre-filled.
```
