import requests
from bs4 import BeautifulSoup
from bs4 import Tag


class News:
    def __init__(self, headline=None, annotation=None, authors=None):
        self.headline = headline
        self.annotation = annotation
        self.authors = authors

    def __str__(self):
        return 'headline: {}\nannotation: {}\nauthors: {}\n'.format(self.headline, self.annotation, self.authors)

    def __hash__(self):
        return self.headline.__hash__()

    def __eq__(self, other):
        return self.headline == other.headline


def is_news_block(tag):
    return tag.has_attr('data-feature-id') and tag['data-feature-id'] == 'homepage/story'


def is_annotation(tag):
    return tag.has_attr('data-pb-field') and tag['data-pb-field'] == 'summary'


def is_headline(tag):
    return tag.has_attr('data-pb-field') and tag['data-pb-field'] == 'web_headline'


def get_washingtonpost_news():
    news = list()
    url = 'http://washingtonpost.com'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    news_blocks = soup.find_all(is_news_block)

    for block in news_blocks:
        headline = block.find(is_headline)
        annotation = block.find(is_annotation)
        authors = block.find_all("span", class_="author vcard")
        authors = list(map(Tag.get_text, authors))

        if annotation is None:
            continue

        news.append(News(headline.get_text(), annotation.get_text(), authors))
    return news


if __name__ == '__main__':
    news = get_washingtonpost_news()
    print(news)