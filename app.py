from wikipedia import wikipedia, PageError
from flask import Flask, request, abort

from schema.author import Author
from schema.book import Book

app = Flask(__name__)


@app.route('/author')
def author_summary():
    name = request.args.get('name')
    try:
        about = wikipedia.summary(name, sentences=3)
        return Author(name, about).to_json()
    except PageError:
        abort(404, description=f'We could not find an author summary for {name}')


@app.route('/book')
def book_summary():
    title = request.args.get('name')
    try:
        blurb = wikipedia.summary(title, sentences=3)
        return Book(title, blurb).to_json()
    except PageError:
        abort(404, description=f'We could not find a book summary for {title}')


if __name__ == '__main__':
    app.run()
