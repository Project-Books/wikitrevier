from wikipedia import wikipedia, PageError
from flask import Flask, request, abort

from schema.author import Author

app = Flask(__name__)


@app.route('/author')
def author_summary():
    name = request.args.get('name')
    try:
        about = wikipedia.summary(name, sentences=3)
        return Author(name, about).to_json()
    except PageError:
        abort(404, description=f'Author {name} not found')



if __name__ == '__main__':
    app.run()
