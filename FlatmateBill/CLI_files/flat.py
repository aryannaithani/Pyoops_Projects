class FlatMates:
    """
    Used for making Flatmate objects with
    parameters name and number of days stayed.
    """

    def __init__(self, name, days, days2, amount):
        self.name = name
        self.days = days
        self.days2 = days2
        self.amount = amount

    def payment(self):
        """
        Calculates the weight of one flatmate and
        uses that to calculate the payable amount
        """

        weight = self.days / (self.days + self.days2)
        return self.amount * weight