import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "http://quotes.toscrape.com"


def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def scrape_quotes():
    quotes_list = []
    authors_info = {}
    page_number = 1
    while True:
        soup = get_soup(f"{BASE_URL}/page/{page_number}/")
        quotes = soup.find_all('div', class_='quote')
        if not quotes:
            break

        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

            quotes_list.append({
                "tags": tags,
                "author": author,
                "quote": text
            })

            if author not in authors_info:
                author_url = BASE_URL + quote.find('a')['href']
                author_soup = get_soup(author_url)
                author_details = author_soup.find('div', class_='author-details')
                fullname = author_details.find('h3', class_='author-title').get_text().strip()
                born_date = author_details.find('span', class_='author-born-date').get_text().strip()
                born_location = author_details.find('span', class_='author-born-location').get_text().strip()
                description = author_details.find('div', class_='author-description').get_text().strip()

                authors_info[author] = {
                    "fullname": fullname,
                    "born_date": born_date,
                    "born_location": born_location,
                    "description": description
                }
        page_number += 1

    return quotes_list, authors_info.values()


quotes, authors = scrape_quotes()

with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump(quotes, f, ensure_ascii=False, indent=4)

with open('authors.json', 'w', encoding='utf-8') as f:
    json.dump(list(authors), f, ensure_ascii=False, indent=4)
