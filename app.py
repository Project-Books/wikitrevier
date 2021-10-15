from wikipedia import wikipedia, PageError, exceptions
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
    # TODO: test
    except exceptions.DisambiguationError as e:
        abort(400, description=f'Your query for {name} was ambiguous. '
                               f'It may refer to any of the following: {e.options}')
    # TODO: test
    except PageError:
        abort(404, description=f'We could not find an author summary for {name}')


# TODO: get genre and notable works, if present
@app.route('/book')
def book_summary():
    title = request.args.get('name')
    try:
        blurb = wikipedia.summary(title, sentences=3)
        return Book(title, blurb).to_json()
    # TODO: test
    except exceptions.DisambiguationError as e:
        abort(400, description=f'Your query for {title} was ambiguous. '
                               f'It may refer to any of the following: {e.options}')
    # TODO: test
    except PageError:
        abort(404, description=f'We could not find a book summary for {title}')


if __name__ == '__main__':
    app.run()
