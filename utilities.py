import requests
import newspaper
from urllib.parse import urlparse


def get_articles(url, source):
    paper = newspaper.build(url)
    print(len(paper.articles))

    for article in paper.articles:
        try:
            article.download()
        except:
            print('Article failed to download')
            continue

        try:
            article.parse()
        except:
            print('Article failed to parse')
            continue

        if validate_article(article):
            try:
                article.nlp()
            except:
                print('Article failed to nlp')
                continue

            if not article.keywords:
                continue

            pub_date = article.publish_date.strftime("%Y-%m-%d")

            parsed_article = {
                'title': article.title,
                'source': source,
                'article_link': article.url,
                'image_link': article.top_image,
                'pub_date': pub_date,
                'keywords': article.keywords,
            }

            post_article(parsed_article)


def validate_article(article):
    if not article.title:
        return False

    if not article.url:
        return False

    if not article.top_image:
        return False

    if not article.publish_date:
        return False

    return True


def post_article(article):
    api = 'http://localhost:8000/articles/'
    r = requests.post(api, data=article)

    print(r.text)
