import requests

def summarize_articles(articles, user_api_key):
    text_input = "\n\n".join([a["text"][:1000] for a in articles])
    prompt = f"""Summarize the following news articles into 50 lines or less.
Group them by category: Politics, Economy, Sports, Technology, World.
Ensure deduplication and clarity:\n\n{text_input}"""

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {user_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/mistral-7b-instruct",  # Free model; fast and high quality
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    
    return result['choices'][0]['message']['content']
