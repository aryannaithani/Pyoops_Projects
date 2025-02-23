from flask.views import MethodView
from wtforms import Form, StringField, SubmitField, validators
from flask import Flask
from flask import render_template, request
import requests
from selectorlib import Extractor

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CalorieFormPage(MethodView):

    def get(self):
        calorie_form = CalorieForm()
        return render_template('calorie-form.html',
                               calorie_form=calorie_form)

    def post(self):
        calorie_form = CalorieForm(request.form)
        weight = float(calorie_form.weight.data)
        height = float(calorie_form.height.data)
        age = int(calorie_form.age.data)
        country = calorie_form.country.data.lower()
        raw_city = calorie_form.city.data.lower().split()
        city = '-'.join(raw_city)

        req = requests.get(f'https://www.timeanddate.com/weather/{country}/{city}')
        extractor = Extractor.from_yaml_file('temperature.yaml')
        temperature = float(extractor.extract(req.text)['temp'].replace('\xa0°C', ''))

        calories = f'{((10*weight)+(6.25*height)-(5*age)-(10*temperature)+5):.2f}'

        return render_template('calorie-form.html',
                               calorie_form=calorie_form,
                               calories=calories,
                               result=True)


class CalorieForm(Form):
    weight = StringField('Weight (in kgs)',[validators.DataRequired()])
    age = StringField('Age',[validators.DataRequired()])
    height = StringField('Height (in cms)',[validators.DataRequired()])
    country = StringField('Country',[validators.DataRequired()])
    city = StringField('City',[validators.DataRequired()])
    button = SubmitField("Calculate",[validators.DataRequired()])


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie-form', view_func=CalorieFormPage.as_view('calorie_form_page'))

app.run(debug=True)