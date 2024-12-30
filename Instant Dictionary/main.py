import requests


class Dictionary:

    def __init__(self, term):
        self.term = term

    def get_definitions(self):
        req = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{self.term}')
        content = req.json()
        return content[0]['meanings'][0]['definitions'][0]['definition']

x = Dictionary('switch')
print(x.get_definitions())