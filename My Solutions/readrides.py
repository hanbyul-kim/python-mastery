import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


import collections

class RideData(collections.Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        return len(self.routes)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self.__getitem__(i) for i in range(index.start or 0, index.stop or len(self), index.step or 1)]
        record = {'route': self.routes[index], 'date': self.dates[index], 'daytype': self.daytypes[index], 'rides': self.numrides[index]}
        return record
    
    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


def read_rides_as_dicts(filename):
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {'route': route, 'date': date, 'daytype': daytype, 'rides': rides}
            records.append(record)
    return records

def read_rides_as_columns(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        routes, dates, daytypes, rides = [], [], [], []
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            rides.append(int(row[3]))
        records = dict(routes=routes, dates=dates, daytypes=daytypes, rides=rides)
    return records

class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_class(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

import typing
class Row2(typing.NamedTuple):
    route: str
    date: str
    daytype: str
    rides: str

def read_rides_as_namedtuple(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row2(route, date, daytype, rides)
            records.append(record)
    return records


class Row3:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_slots(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row3(route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    # rows = read_rides_as_tuples('Data/ctabus.csv')
    rows = read_rides_as_dicts('Data/ctabus.csv')
    # rows = read_rides_as_class('Data/ctabus.csv')
    # rows = read_rides_as_namedtuple('Data/ctabus.csv')
    # rows = read_rides_as_slots('Data/ctabus.csv')
    # rows = read_rides_as_columns('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())