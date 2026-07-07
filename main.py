from finnhub_client import get_news
from summary import summarize_news


def main():

    data = []
    articles = get_news()

    article = summarize_news(articles[i]["headline"], articles[i]["url"])
    data.append(article)

    return data 




if __name__ == "__main__":
    main()




