from FlatmateBill.CLI_files.flat import FlatMates
from FlatmateBill.CLI_files.pdf import PdfGenerator

amount = int(input("Please enter the bill amount: "))
period = input("Please enter the bill period: ").capitalize()
name1 = input("What is your name?: ").capitalize()
days1 = int(input("How many days did you stay in the house: "))
name2 = input("What is the name of the other flatmate?: ").capitalize()
days2 = int(input(f"How many days did {name2} stay in the house: "))

mate1 = FlatMates(name1, days1, days2, amount)
mate2 = FlatMates(name2, days2, days1, amount)
bill = PdfGenerator(name1, name2, days1, days2, amount, period, mate1, mate2)

print(f"You have to pay : {mate1.payment():.2f}")
print(f"{name2} has to pay : {mate2.payment():.2f}")

bill.generate_pdf()