from FlatmateBill.CLI_files.flat import name2, mate1, mate2
from FlatmateBill.CLI_files.pdf import PdfGenerator

bill = PdfGenerator()
print(f"You have to pay : {mate1.payment():.2f}")
print(f"{name2} has to pay : {mate2.payment():.2f}")
bill.generate_pdf()