from filestack import Client
from fpdf import FPDF

class PdfGenerator:
    """
    Generates a .pdf file of the bill in the main directory
    with information regarding both flatmates and the bill
    and provides a link to the pdf
    """

    def __init__(self, name1, name2, days1, days2, amount, period, mate1, mate2):
        self.name1 = name1
        self.name2 = name2
        self.days1 = days1
        self.days2 = days2
        self.amount = amount
        self.period = period
        self.mate1 = mate1
        self.mate2 = mate2


    def generate_pdf(self):
        pdf = FPDF(orientation='P', format='A4', unit='pt')
        pdf.add_page()
        pdf.set_font(family='Times', style='B', size=30)
        pdf.cell(w=0, h=75, txt='BILL SHARING', align='C', ln=1)
        pdf.set_font(family='Times', style='B', size=25)
        pdf.cell(w=0, h=75, align='C', ln=1, txt=f'Total Bill : {self.amount}')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=0, h=75, align='C', ln=1, txt=f'Bill Period: {self.period}')
        pdf.cell(w=269, h=75, align='C', txt='Flat Mate - 1', border=1)
        pdf.cell(w=269, h=75, align='C', txt='Flat Mate - 2', ln=1, border=1)
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=94, h=75, txt='Name: ', border=1, align='C')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{self.name1}', border=1, align='C')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=94, h=75, txt='Name: ', border=1, align='C')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{self.name2}', ln=1, border=1, align='C')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=94, h=75, txt='Days: ', border=1, align='C')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{self.days1}', border=1, align='C')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=94, h=75, txt='Days: ', border=1, align='C')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{self.days2}', ln=1, border=1, align='C')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=94, h=75, txt='Amount: ', border=1, align='C')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{self.mate1.payment():.2f}', border=1, align='C')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=94, h=75, txt='Amount: ', border=1, align='C')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{self.mate2.payment():.2f}', ln=1, border=1, align='C')
        pdf.line(x1=50, y1=600, x2=545, y2=600)
        pdf.output('bill.pdf')
        client = Client('AxG9Oi03qTq6UJue2O5npz')
        link = client.upload(filepath='bill.pdf')
        return link.url
