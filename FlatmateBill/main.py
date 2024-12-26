from flask.views import MethodView
from wtforms import Form
from flask import Flask
from flask import render_template

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        return render_template('bill-form.html')


class ResultPage(MethodView):

    def get(self):
        pass


class BillForm(Form):
    pass


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill-form', view_func=BillFormPage.as_view('bill_form_page'))

app.run(debug=True)