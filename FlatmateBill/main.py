from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask
from flask import render_template, request
from CLI_files import flat

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill-form.html', bill_form=bill_form)


class ResultPage(MethodView):

    def post(self):
        bill_form = BillForm(request.form)
        amount = int(bill_form.amount.data)
        period = bill_form.period.data
        name1 = bill_form.name1.data
        name2 = bill_form.name2.data
        days1 = int(bill_form.days1.data)
        days2 = int(bill_form.days2.data)

        mate1 = flat.FlatMates(name1, days1, days2, amount)
        mate2 = flat.FlatMates(name2, days2, days1, amount)
        return render_template('result-page.html',
                               name1=name1,
                               name2=name2,
                               amount1=f'{mate1.payment():.2f}',
                               amount2=f'{mate2.payment():.2f}')


class BillForm(Form):
    amount = StringField('Bill Amount: ')
    period = StringField('Bill Period: ')
    name1 = StringField('Name: ')
    days1 = StringField('No. of Days: ')
    name2 = StringField('Name: ')
    days2 = StringField('No. of Days: ')
    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill-form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/result-page', view_func=ResultPage.as_view('result_page'))

app.run(debug=True)