import requests
from dotenv import load_dotenv
import os



load_dotenv()

API_KEY = os.environ["FINNHUB_API_KEY"]
BASE_URL = "https://finnhub.io/api/v1"

def get_news(category="general"):

    try: 
        url = f"{BASE_URL}/news?category={category}&token={API_KEY}"
    
        response = requests.get(url)
        data = response.json()
   
        return data
    
    except Exception as e: 
        print("Error fetching data", e)
        raise



