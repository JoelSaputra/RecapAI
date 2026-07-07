import time
from finnhub_client import get_news
from summary import summarize_news, filter_articles
from fastapi import FastAPI

app = FastAPI()

@app.get("/news-getter")
def main():
    try:
        articles = get_news()
        filtered_articles = filter_articles(articles)  
        summarized_articles = summarize_news(filtered_articles)
        
        return summarized_articles
    
    except Exception as e: 
        print("Error", e)
    


if __name__ == "__main__":
    main()




