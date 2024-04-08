from Euro import Euro
# from Dollar import Dollar
class Shekel(object):
    def __init__(self, value):
        D = Euro(value)
        self._value = value
        self.rates = D.rates
    def __repr__(self):
        return f'Shekel{self._value}'
    def __str__(self):
        return 'Shekel(value: {})'.format(self._value)
    def amount (self):
        return self._value

    def __add__(self, other):
        return self.amount() + other.amount()
    def get_value(self):
        return self._value
    def __sub__(self, other):
        return self.amount() - other.amount()