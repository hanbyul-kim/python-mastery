# stock.py
import csv

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

def read_portfolio(filename):
    ret = []
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            ret.append(Stock(row[0], int(row[1]), float(row[2])))
    return ret

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ("names", "shares", "price"))
    print('%10s %10s %10s' % ("-"*10, "-"*10, "-"*10))
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))