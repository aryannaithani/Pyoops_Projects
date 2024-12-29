import requests
import yagmail
import pandas


class Articles:

    def __init__(self, interest, name):
        self.interest = interest
        self.name = name
        self.req = requests.get(f'https://newsapi.org/v2/everything?'
                                f'q={self.interest}&'
                                f'language=en&'
                                f'apiKey=f70aa27ddfb74c35a284523c3361afb3')
        self.content = self.req.json()

    def get(self):
        out = ''
        for i in range(10):
            out += self.content['articles'][i]['title']+'\n'+self.content['articles'][i]['url']+'\n\n'
        return out


mail = yagmail.SMTP(user='aryannaithani1085@gmail.com',
                    password='enaexcwqwfkpizao')
df = pandas.read_excel('people.xlsx')
for index, row in df.iterrows():
    subject = f'Hello {row['name']}, Here is your news regarding {row['interest']}'
    x = Articles(row['interest'], row['name'])
    mail.send(to=row['email'],
              contents=x.get(),
              subject=subject)
