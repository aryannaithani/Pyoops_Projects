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


class Email:
    def __init__(self):
        self.mail = yagmail.SMTP(user='aryannaithani1085@gmail.com',
                                 password='enaexcwqwfkpizao')
        self.data_frame = pandas.read_excel('people.xlsx')

    def send(self):
        for index, row in self.data_frame.iterrows():
            subject = f'Hello {row['name']}, Here is your news regarding {row['interest']}'
            x = Articles(row['interest'], row['name'])
            self.mail.send(to=row['email'],
                           contents=x.get(),
                           subject=subject)


sender = Email()
sender.send()