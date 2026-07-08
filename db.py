import sqlite3
import json


DB_FILE = "news.db"

def get_connection():
   return sqlite3.connect(DB_FILE)



def create_table():
   conn = get_connection()
   cursor = conn.cursor()

   cursor.execute("""
        CREATE TABLE IF NOT EXISTS news(
            url TEXT PRIMARY KEY,
            headline TEXT, 
            bullets TEXT, 
            image TEXT
        )
    """)
   
   conn.commit()
   conn.close()




def replace_articles(articles):
   conn = get_connection()
   cursor = conn.cursor()

   cursor.execute("DELETE FROM news")
   for article in articles:
      cursor.execute(
         "INSERT INTO news(url, headline, bullets, image) VALUES (?, ?, ?, ?)",
         (
            article["url"],
            article["headline"],
            json.dumps(article["bullets"]),
            article["image"]
         ),
      )
   conn.commit()
   conn.close()



def get_articles():
   conn = get_connection()
   cursor = conn.cursor()

   cursor.execute("SELECT url, headline, bullets, image FROM news")
   rows = cursor.fetchall()
   
   conn.close()


   articles = []
   for url, headline, bullets, image in rows:
      articles.append({
         "url": url,
         "headline": headline,
         "bullets": json.loads(bullets),
         "image": image,
      })


   return articles
   

    
    


      

    

    