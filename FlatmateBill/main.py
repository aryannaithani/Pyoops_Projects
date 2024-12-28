from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask
from flask import render_template, request
from CLI_files import flat
from CLI_files import pdf

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()

        return render_template('bill-form.html', bill_form=bill_form)

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
        bill_pdf = pdf.PdfGenerator(name1, name2, days1, days2, amount, period, mate1, mate2)

        return render_template('bill-form.html',
                               result=True,
                               bill_form=bill_form,
                               name1=name1,
                               name2=name2,
                               amount1=f'{mate1.payment():.2f}',
                               amount2=f'{mate2.payment():.2f}',
                               link=bill_pdf.generate_pdf())


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

app.run(debug=True)