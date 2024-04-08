# from Dollar import Dollar
# from Shekel import Shekel

dollar_to_nis = float(input("enter Conversion rates between dollar to nis: "))
euro_to_nis = float(input("enter Conversion rates between euro to nis: "))


class Euro(object):

    def __init__(self, value):
        self._value = value
        self.rates = {("dollar, nis"): dollar_to_nis,("euro,nis"): euro_to_nis}
        self.rates = {("dollar, nis"): dollar_to_nis,("euro,nis"): euro_to_nis,("dollar, euro") : self.rates[("dollar, nis")]/ self.rates[("euro,nis")],
                      ("euro, dollar"): self.rates[("euro,nis")]/self.rates[("dollar, nis")], ("nis, dollar") : 1/self.rates[("dollar, nis")], ("nis, euro"): 1/self.rates[("euro,nis")]}
    def __repr__(self):
        return 'Euro(value={})'.format(self._value)
    def __str__(self):
        return 'Euro(value: {})'.format(self._value)
    def amount (self):
        return self._value*self.rates["euro,nis"]
    def __add__(self, other):
        return self.amount() + other.amount()
    def get_value(self):
        return self._value
    def set_value(self, value):
        self._value =  float(value*float(self.rates[("nis, euro")]))
    def __sub__(self, other):
        return self.amount() - other.amount()
