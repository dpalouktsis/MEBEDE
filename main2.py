import random
import math


class Model:
    # instance variables
    def __init__(self):
        self.allVehicles = []
        self.allNodes = []
        self.customers = []
        self.visited = []
        self.unvisited = []
        self.matrix = []
        self.total_profit = 0

    def max_profit(self):
        unvisited_length = len(self.unvisited)
        vehicles_length = len(self.allVehicles)
        while vehicles_length > 0:
            for vindex in range(0, vehicles_length-1):
                if self.allVehicles[vindex].q > 0 and self.allVehicles[vindex].t <= 200:
                    vind = vindex
                    while unvisited_length > 0:
                        mp = -1
                        ind = 0
                        for index in range(0, unvisited_length):
                            if self.unvisited[index].p > mp:
                                mp = self.unvisited[index].p
                                ind = index  # keep index of customer that has it and return it
                        self.visited.append(self.unvisited[ind])
                        dist = math.sqrt(math.pow(self.unvisited[ind].x - self.allVehicles[vind].x, 2) +
                                         math.pow(self.unvisited[ind].y - self.allVehicles[
                                                                                               vind].y, 2))
                        self.allVehicles[vind].t += self.unvisited[ind].st + dist
                        self.allVehicles[vind].x = self.unvisited[ind].x
                        self.allVehicles[vind].y = self.unvisited[ind].y
                        self.allVehicles[vind].q -= self.unvisited[ind].d
                        self.total_profit += self.unvisited[ind].p
                        self.unvisited.pop(
                            ind)  # remove the element from the unvisited list (This may need to be done later)
                        unvisited_length = len(self.unvisited)
                        mp = -1
                        if self.allVehicles[vind].q <= 0 or self.allVehicles[vind].t > 200:
                            self.allVehicles.pop(vind)
                            vehicles_length = len(self.allVehicles)
        return self.total_profit

    def distance(self, x1, y1, x2, y2):
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return d

    def BuildModel(self, n, k, Q, T, xdep, ydep):
        random.seed(10)
        depot = Node(0, xdep, ydep)
        self.allNodes.append(depot)

        totalCustomers = n
        totalVehicles = k

        for i in range(0, totalVehicles):
            veh = Vehicles(i + 1, xdep, ydep, Q, 0)
            self.allVehicles.append(veh)

        for i in range(0, totalCustomers):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            d = random.randint(0, 100)
            st = random.randint(0, 100)
            p = random.randint(0, 100)
            cust = Customer(i + 1, x, y, d, st, p)
            self.customers.append(cust)
            self.unvisited.append(cust)

        for counter in range(len(self.customers)):
            print(self.customers[counter])

        for counter1 in range(len(self.allVehicles)):
            print(self.allVehicles[counter1])

        # rows = len(self.allNodes)
        # self.matrix = [[0.0 for x in range(rows)] for y in range(rows)]

        # for i in range(0, len(self.allNodes)):
        #    for j in range(0, len(self.allNodes)):
        #       a = self.allNodes[i]
        #        b = self.allNodes[j]
        #        dist = math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))
        #        self.matrix[i][j] = dist


class Node:
    def __init__(self, idd, xx, yy):
        self.x = xx
        self.y = yy
        self.ID = idd
        self.isRouted = False


class Customer:
    def __init__(self, idd, xx, yy, dd, stt, pp):
        self.x = xx
        self.y = yy
        self.ID = idd
        self.d = dd
        self.st = stt
        self.p = pp
        self.isRouted = False


class Vehicles:
    def __init__(self, iddd, xxx, yyy, qqq, ttt):
        self.id = iddd
        self.x = xxx
        self.y = yyy
        self.q = qqq
        self.t = ttt


m = Model()
m.BuildModel(5, 2, 150, 200, 23.142, 11.736)
print(m.max_profit())

print('test')
