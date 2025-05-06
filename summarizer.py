import requests

def summarize_articles(articles, user_api_key):
    text_input = "\n\n".join([a["text"][:500] for a in articles])  # Optional: increase if needed
    prompt = (
        "Summarize the following news articles in under 100 words. "
        "Group by category: Politics, Economy, Sports, Technology, World. "
        "Avoid repetition, focus on clarity and key facts:\n\n" + text_input
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
