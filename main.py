import time
from finnhub_client import get_news
from summary import summarize_news, filter_articles
from fastapi import FastAPI, HTTPException
from db import create_table, replace_articles, get_articles
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/news-getter")
def get_news():
    try:
        articles = get_news()
        filtered_articles = filter_articles(articles)  
        summarized_articles = summarize_news(filtered_articles)
        
        replace_articles(summarized_articles)
    
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"Failed to fetch summarized news: {e}")
    


@app.get("/news")
def get_news_endpoint():
    return get_articles()

    







