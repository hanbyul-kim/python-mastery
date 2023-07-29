import csv

def read_csv_as_dicts(filename, types):
    with open(filename) as f:
        header = next(f).strip().split(',')

        records = []
        for row in f:
            records.append({name: func(val) for name, func, val in zip(header, types, row.split(','))})

        return records


def read_csv_as_instances(filename, cls):
    ret = []
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            ret.append(cls.from_row(row))
    return ret

if __name__ == "__main__":
    import tracemalloc
    from sys import intern
    tracemalloc.start()
    portfolio = read_csv_as_dicts('Data/ctabus.csv', [intern,intern,str,int])
    # for s in portfolio:
        # print(s)
    print(tracemalloc.get_traced_memory())