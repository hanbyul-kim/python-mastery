# stock.py
import csv

class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares


def print_portfolio(portfolio):
    print('%10s %10s %10s' % ("names", "shares", "price"))
    print('%10s %10s %10s' % ("-"*10, "-"*10, "-"*10))
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))