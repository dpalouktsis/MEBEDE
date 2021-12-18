import itertools
import math
from itertools import count

sequence = count(start=1, step=1)

unvisited = []
total_profit = 0
all_customers = []


class Vehicles:
    id_iter = itertools.count()

    def __init__(self, x, y, q, t):
        self.id = next(self.id_iter) + 1
        self.x = x
        self.y = y
        self.q = q
        self.t = t

    def get_q(self):
        return self.q

    def get_t(self):
        return self.t


class Customers:
    id_iter = itertools.count()

    def __init__(self, x, y, d, st, p):
        self.id = next(self.id_iter) + 1
        self.x = x
        self.y = y
        self.d = d
        self.st = st
        self.p = p


c1 = Customers(74.116, 71.636, 3, 11, 1)
all_customers.append(c1)
unvisited.append(c1)
c2 = Customers(-26.902, -6.824, 4, 7, 3)
unvisited.append(c2)
all_customers.append(c2)
c3 = Customers(-80.364, 14.724, 22, 14, 23)
unvisited.append(c3)
all_customers.append(c3)
c4 = Customers(24.198, 75.815, 19, 7, 13)
unvisited.append(c4)
all_customers.append(c4)
c5 = Customers(43.53, 54.191, 19, 16, 8)
unvisited.append(c5)
all_customers.append(c5)

k1 = Vehicles(23.142, 11.736, 150, 0)
k2 = Vehicles(23.142, 11.736, 150, 0)
k3 = Vehicles(23.142, 11.736, 150, 0)
k4 = Vehicles(23.142, 11.736, 150, 0)
k5 = Vehicles(23142, 11.736, 150, 0)
k6 = Vehicles(23.142, 11.736, 150, 0)


def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d


visited = []


def max_profit():
    global unvisited
    unvisited_length = len(unvisited)
    mp = -1
    for i in range(1, unvisited_length):
        if unvisited[i - 1].p > mp:
            mp = unvisited[i - 1].p
            ind = i  # keep index of customer that has it and return it
    return ind


def less_time(unvisited):
    unvisited_length = len(unvisited)
    lt = 99999
    for i in range(1, unvisited_length):
        if unvisited[i - 1].st < lt:
            lt = unvisited[i - 1].st
            ind = i  # keep index of customer that has it and return it
    return ind


test = distance(-5, 10, 17, 2)
print(test)

print(k2.id)

print(max_profit())  # we run this when we need to find the next max profit node's index to visit
print(less_time(unvisited))


# listToStr = ' '.join([str(elem) for elem in all_customers])
# print(listToStr)


# def ret_Customer(node_ind):
#   for i in range(all_customers):
#      if (node_ind = ):


def find_next_customer():  # BRISKEI TO KALUTERO PROFIT KAI PHGAINEI TO FORTHGO POU TOU BAZOUME EKEI ALLAZONTAS KAI
    # TA STOIXEIA TOU
    next_id = max_profit()
    global total_profit
    global unvisited
    global k1
    for x in unvisited:
        if x.id == next_id:
            k1 = (x.x, x.y, k1.q - x.d, k1.t + x.st + distance(k1.x, k1.y, x.x, x.y))  # auth h grammh einai lathos
            total_profit = total_profit + x.p
            unvisited.pop(x.id)
            visited.append(x)
            return x


while len(unvisited) > 0:
    cust = find_next_customer()  # takes the tuple from the above def and returns both the next customer
    # while also changing the vehicles elements

print(cust.id)
print(total_profit)
