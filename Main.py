
from Euro import Euro
from Dollar import Dollar
from Shekel import Shekel


def add(coin1, coin2):
    temp = coin1 + coin2
    type_coin = type(coin1)
    if type_coin == Dollar:
        s = Dollar(temp)
        s.set_value(temp)
        return s
    elif type_coin == Euro:
        s = Euro(temp)
        s.set_value(temp)
        return s
    else:
        s = Shekel(temp)
        return s


def sub(coin1, coin2):
    temp = coin1 - coin2
    if temp < 0:
        raise TypeError("coins sum must be non negative")
    type_coin = type(coin1)
    if type_coin == Dollar:
        s = Dollar(temp)
        s.set_value(temp)
        return s
    elif type_coin == Euro:
        s = Euro(temp)
        s.set_value(temp)
        return s
    else:
        s = Shekel(temp)
        return s



def apply(oprator_name, coin1, coin2):
    return (eval(oprator_name)(coin1, coin2))


def coerce_apply(oprator_name, coin1, coin2):
    return Shekel((eval(oprator_name)(coin1, coin2)).amount())
if __name__ == '__main__':
        s = Shekel(50)
        d = Dollar(50)
        e = Euro(50)
        print(d.amount())
        print(e.amount())
        print(d + s)
        print(add(d, e))
        print(sub(e, d))
        z = eval(repr(d))
        print(z.amount())
        print(apply('add', s, d))

        print(apply('add', Dollar(50), Euro(20)))
        print(apply('sub', Dollar(50), Euro(20)))
        print(coerce_apply('add', Dollar(50), Euro(20)))
        print(coerce_apply('sub', Dollar(50),Euro(20)))
    # s = Shekel(50)
    # d = Dollar(50)
    # e = Euro(20)
    # print(d.amount())
    # print(e.rates)
    #
    # print(e.amount())
    # print(d + s)
    #
    #
    # z = eval(repr(d))
    # print(z)
    # print(s)
    # print(e)


    #
    # print(apply('add',d,e))
    # print(coerce_apply('sub',d,e))
    # print(coerce_apply('sub', Dollar(50), Euro(20)))
