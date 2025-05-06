from newspaper import Article

def scrape_articles(urls):
    articles = []
    for url in urls:
        try:
            article = Article(url)
            article.download()
            article.parse()
            articles.append({"title": article.title, "text": article.text})
        except Exception:
            continue
    return articles
