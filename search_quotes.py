from models import Quote
import sys

def search_by_author(author_name):
    quotes = Quote.objects(author__fullname=author_name)
    for quote in quotes:
        print(quote.quote.encode('utf-8'))

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    for quote in quotes:
        print(quote.quote.encode('utf-8'))

def search_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    for quote in quotes:
        print(quote.quote.encode('utf-8'))

if __name__ == '__main__':
    while True:
        command = input("Enter command: ")
        if command.startswith("name:"):
            author_name = command[len("name:"):].strip()
            search_by_author(author_name)
        elif command.startswith("tag:"):
            tag = command[len("tag:"):].strip()
            search_by_tag(tag)
        elif command.startswith("tags:"):
            tags = command[len("tags:"):].strip()
            search_by_tags(tags)
        elif command == "exit":
            sys.exit()
        else:
            print("Unknown command")
