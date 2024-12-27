from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask
from flask import render_template, request

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CalorieFormPage(MethodView):

    def get(self):
        calorie_form = CalorieForm()
        return render_template('calorie-form.html', calorie_form=calorie_form)


class CalorieForm(Form):
    weight = StringField('Weight (in kgs)')
    age = StringField('Age')
    height = StringField('Height (in cms)')
    country = StringField('Country')
    city = StringField('City')
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie-form', view_func=CalorieFormPage.as_view('calorie_form_page'))

app.run(debug=True)