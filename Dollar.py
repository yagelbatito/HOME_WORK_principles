from Euro import Euro
from Shekel import Shekel

class Dollar(object):
    def __init__(self, value):
        D = Euro(value)
        self._value = value
        self.rates = D.rates
    def __repr__(self):
        return f'Dollar(value={self._value})'
    def __str__(self):
        return 'Dollar(value: {})'.format(self._value)
    def amount (self):
        return self._value*self.rates["dollar, nis"]

    def __add__(self, other):
        return self.amount() + other.amount()
    def __sub__(self, other):
        return self.amount() - other.amount()
    def get_value(self):
        return self._value
    def set_value(self, value):
        self._value =  float(value*float(self.rates[("nis, dollar")]))