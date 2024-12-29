import requests
import yagmail


class Articles:

    def __init__(self, interest):
        self.interest = interest
        self.req = requests.get(f'https://newsapi.org/v2/everything?'
                                f'q={self.interest}&'
                                f'language=en&'
                                f'apiKey=f70aa27ddfb74c35a284523c3361afb3')
        self.content = self.req.json()

    def get(self):
        out = f'Hello xyz\nHere is the latest news about {self.interest}\n\n'
        for i in range(10):
            out += self.content['articles'][i]['title']+'\n'+self.content['articles'][i]['url']+'\n\n'
        return out


mail = yagmail.SMTP(user='aryannaithani1085@gmail.com',
                    password='aryanyuvi5')
x = Articles('nasa')
mail.send(to='aryannaithani2002@gmail.com',
          contents=x.get())
