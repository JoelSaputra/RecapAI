import time
from finnhub_client import get_news
from summary import summarize_news
from fastapi import FastAPI

app = FastAPI()

@app.get("/news-getter")
def main():
    data = []
    articles = get_news()

    for article in articles[:2]: 
        summary = summarize_news(article["headline"], article["summary"])
        data.append(summary)
        time.sleep(5)  # ~12 requests/minute, safely under Gemini 3.1 Flash Lite's 15 RPM limit

    return data


if __name__ == "__main__":
    main()




