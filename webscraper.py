from urls import URLS
from newspaper import Article
import pandas as pd


def get_text_and_date(link):
    article = Article(link)
    article.download()
    article.parse()
    return article.text, article.publish_date


def gen_data():
    datastore = []
    for newspaper in URLS:
        print(f'Scraping {newspaper}')
        for i, url in enumerate(URLS[newspaper]):
            try:
                text, date = get_text_and_date(url)
                datastore.append([newspaper, text, date])
            except:
                print(f'-------- Couldn\'t get {url} :/')
                pass
            print(f'--------- {int(100 * (i+1)/len(URLS[newspaper]))}% done')
    df = pd.DataFrame(columns=['newspaper', 'text', 'date'], data=datastore)
    return df


if __name__ == '__main__':
    df = gen_data()
    df.to_csv('./data/news.csv', sep='~', index=False)

