import requests
import justpy as jp


class Dictionary:

    def get_definitions(self, term):
        req = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{term}')
        content = req.json()
        return content[0]['meanings'][0]['definitions'][0]['definition']


@jp.SetRoute('/')
def homepage():
    wp = jp.WebPage()
    container = jp.Div(a=wp, classes='bg-gray-400 h-screen p-4')
    div1 = jp.Div(a=container, classes='grid grid-cols-1 gap-3 place-items-center')
    jp.H1(a=div1, text='(not so) Instant Dictionary', classes='text-5xl py-5 font-bold')
    term = jp.Input(a=div1, placeholder='Enter a Word...', classes='rounded w-1/4')
    output = jp.Div(a=div1)
    jp.Button(a=div1, text='Define', click=define, term=term, output=output,
              classes='rounded px-3 py-1 border border-black')

    return wp

def define(widget, msg):
    x = Dictionary()
    widget.output.text = x.get_definitions(widget.term.value)

jp.justpy()