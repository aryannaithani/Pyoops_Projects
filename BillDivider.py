from fpdf import FPDF

class Bill:

    def __init__(self, l_amount, l_period):
        self.amount = l_amount
        self.period = l_period


class FlatMates:

    def __init__(self, name, days):
        self.name = name
        self.days = days

    def payment(self):
        weight = self.days / (mate1.days + mate2.days)
        return the_bill.amount * weight


class PdfGenerator:

    def generate_pdf(self):
        pdf = FPDF(orientation='P', format='A4', unit='pt')
        pdf.add_page()
        pdf.set_font(family='Times', style='B', size=30)
        pdf.cell(w=550, h=75, txt='BILL SHARING', align='C', ln=1)
        pdf.set_font(family='Times', style='B', size=25)
        pdf.cell(w=550, h=75, align='C', ln=1, txt=f'Total Bill : {the_bill.amount}')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=550, h=75, align='C', ln=1, txt=f'Bill Period: {the_bill.period}')
        pdf.cell(w=275, h=75, align='C', txt='Flat Mate - 1')
        pdf.cell(w=275, h=75, align='C', txt='Flat Mate - 2', ln=1)
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=100, h=75, txt='Name: ')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{mate1.name}')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=100, h=75, txt='Name: ')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{mate2.name}', ln=1)
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=100, h=75, txt='Days: ')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{mate1.days}')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=100, h=75, txt='Days: ')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{mate2.days}', ln=1)
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=100, h=75, txt='Amount: ')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{mate1.payment():.2f}')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=100, h=75, txt='Amount: ')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{mate1.payment():.2f}', ln=1)
        pdf.line(x1=50, y1=600, x2=545, y2=600)
        pdf.output('bill.pdf')


amount = int(input("Please enter the bill amount: "))
period = input("Please enter the bill period: ").capitalize()
name1 = input("What is your name?: ").capitalize()
days1 = int(input("How many days did you stay in the house: "))
name2 = input("What is the name of the other flatmate?: ").capitalize()
days2 = int(input(f"How many days did {name2} stay in the house: "))
the_bill = Bill(amount, period)
mate1 = FlatMates(name1, days1)
mate2 = FlatMates(name2, days2)
bill = PdfGenerator()
print(f"You have to pay : {mate1.payment():.2f}")
print(f"{name2} has to pay : {mate2.payment():.2f}")
bill.generate_pdf()