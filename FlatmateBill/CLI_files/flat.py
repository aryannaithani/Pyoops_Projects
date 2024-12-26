class Bill:
    """
    Generates a basic bill object with all the basic bill
    information like the amount and the period of the bill.
    """

    def __init__(self, l_amount, l_period):
        self.amount = l_amount
        self.period = l_period


class FlatMates:
    """
    Used for making Flatmate objects with
    parameters name and number of days stayed.
    """

    def __init__(self, name, days):
        self.name = name
        self.days = days

    def payment(self):
        """
        Calculates the weight of one flatmate and
        uses that to calculate the payable amount
        """

        weight = self.days / (mate1.days + mate2.days)
        return the_bill.amount * weight


amount = int(input("Please enter the bill amount: "))
period = input("Please enter the bill period: ").capitalize()
name1 = input("What is your name?: ").capitalize()
days1 = int(input("How many days did you stay in the house: "))
name2 = input("What is the name of the other flatmate?: ").capitalize()
days2 = int(input(f"How many days did {name2} stay in the house: "))
the_bill = Bill(amount, period)
mate1 = FlatMates(name1, days1)
mate2 = FlatMates(name2, days2)
