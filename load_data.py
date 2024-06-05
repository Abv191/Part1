import json
from models import Author, Quote

# Завантаження даних авторів
with open('authors.json', 'r') as f:
    authors_data = json.load(f)
    for author_data in authors_data:
        author = Author(
            fullname=author_data['fullname'],
            born_date=author_data['born_date'],
            born_location=author_data['born_location'],
            description=author_data['description']
        )
        author.save()

# Завантаження даних цитат
with open('qoutes.json', 'r') as f:
    quotes_data = json.load(f)
    for quote_data in quotes_data:
        author = Author.objects(fullname=quote_data['author']).first()
        if author:
            quote = Quote(
                tags=quote_data['tags'],
                author=author,
                quote=quote_data['quote']
            )
            quote.save()
