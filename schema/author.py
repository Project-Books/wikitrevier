import json


class Author:
    def __init__(self, name, about=None):
        self.name = name
        self.about = about

    def to_json(self):
        return json.dumps(self, default=lambda a: a.__dict__)


