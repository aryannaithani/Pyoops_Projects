from filestack import Client
from fpdf import FPDF

from FlatmateBill.CLI_files.flat import the_bill, mate1, mate2


class PdfGenerator:
    """
    Generates a .pdf file of the bill in the main directory
    with information regarding both flatmates and the bill
    and provides a link to the pdf
    """

    def generate_pdf(self):
        pdf = FPDF(orientation='P', format='A4', unit='pt')
        pdf.add_page()
        pdf.set_font(family='Times', style='B', size=30)
        pdf.cell(w=0, h=75, txt='BILL SHARING', align='C', ln=1)
        pdf.set_font(family='Times', style='B', size=25)
        pdf.cell(w=0, h=75, align='C', ln=1, txt=f'Total Bill : {the_bill.amount}')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=0, h=75, align='C', ln=1, txt=f'Bill Period: {the_bill.period}')
        pdf.cell(w=269, h=75, align='C', txt='Flat Mate - 1', border=1)
        pdf.cell(w=269, h=75, align='C', txt='Flat Mate - 2', ln=1, border=1)
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=94, h=75, txt='Name: ', border=1, align='C')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{mate1.name}', border=1, align='C')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=94, h=75, txt='Name: ', border=1, align='C')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{mate2.name}', ln=1, border=1, align='C')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=94, h=75, txt='Days: ', border=1, align='C')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{mate1.days}', border=1, align='C')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=94, h=75, txt='Days: ', border=1, align='C')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{mate2.days}', ln=1, border=1, align='C')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=94, h=75, txt='Amount: ', border=1, align='C')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{mate1.payment():.2f}', border=1, align='C')
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=94, h=75, txt='Amount: ', border=1, align='C')
        pdf.set_font(family='Times', size=20)
        pdf.cell(w=175, h=75, txt=f'{mate2.payment():.2f}', ln=1, border=1, align='C')
        pdf.line(x1=50, y1=600, x2=545, y2=600)
        pdf.output('Bills/bill.pdf')
        client = Client('AxG9Oi03qTq6UJue2O5npz')
        link = client.upload(filepath='../Bills/bill.pdf')
        print(link.url)
