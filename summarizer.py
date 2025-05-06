import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_articles(articles):
    text_input = "\n\n".join([a["text"][:1000] for a in articles])
    prompt = f"""Summarize the following news articles into 50 lines or less.
Group them by category: Politics, Economy, Sports, Technology, World.
Ensure deduplication and clarity:\n\n{text_input}"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
