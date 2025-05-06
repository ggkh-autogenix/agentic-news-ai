from openai import OpenAI

def summarize_articles(articles, user_api_key):
    text_input = "\n\n".join([a["text"][:1000] for a in articles])
    prompt = f"""Summarize the following news articles into 50 lines or less.
Group them by category: Politics, Economy, Sports, Technology, World.
Ensure deduplication and clarity:\n\n{text_input}"""

    # Initialize OpenAI client with user-provided key
    client = OpenAI(api_key=user_api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
