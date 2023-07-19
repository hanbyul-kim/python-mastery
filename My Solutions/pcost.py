def portfolio_cost(filename):
    ans = 0
    with open(filename) as f:
        for line in f.readlines():
            ticker, num, price = line.split()
            if num == '-':
                continue
            ans += int(num) * float(price)
    return ans

if __name__ == "__main__":
    print(portfolio_cost('Data/portfolio2.dat'))