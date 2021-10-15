import json


class Book:
    def __init__(self, title, blurb):
        self.title = title
        self.blurb = blurb

    def to_json(self):
        return json.dumps(self, default=lambda a: a.__dict__)
