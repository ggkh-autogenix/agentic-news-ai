# Agentic News Summarizer AI

This project uses GPT to read multiple newspaper websites, summarize them by category (Politics, Economy, Tech, etc.), compare articles for consistency, and sends the result via WhatsApp to a dynamic phone number using Twilio.

## Features
- News scraped from dynamic URLs
- AI-powered summarization (GPT-4)
- WhatsApp summary delivery (Twilio)
- Free deployment using Replit or Render

## Setup
1. Add your API keys to `.env` or Replit/Render secrets:
   - `OPENAI_API_KEY`
   - `TWILIO_SID`
   - `TWILIO_TOKEN`
   - `TWILIO_WHATSAPP`

2. Deploy to [Render](https://render.com) or [Replit](https://replit.com)

## API Example

POST `/daily-summary`
```json
{
  "urls": ["https://example.com/news1", "https://example.com/news2"],
  "phone": "+911234567890"
}
```
