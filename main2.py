import random
import math
import csv

file = open(r"C:\Users\dimpa\Documents\csvfile.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()


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
        self.timecon = 0
        self.dict = {}

    def max_profit(self):
        unvisited_length = len(self.unvisited)
        vehicles_length = len(self.allVehicles)
        s = True
        if s:
            for vindex in range(0, vehicles_length):
                bool = True
                if self.allVehicles[vindex].q > 0 and self.allVehicles[vindex].t < self.timecon:
                    vind = vindex
                    while unvisited_length > 0 and bool:
                        mp = -1
                        ind = 0
                        for index in range(0, unvisited_length):
                            if self.unvisited[index].p > mp:
                                mp = self.unvisited[index].p
                                ind = index  # keep index of customer that has it and return it
                        dist = math.sqrt(math.pow(self.unvisited[ind].x - self.allVehicles[vind].x, 2) +
                                         math.pow(self.unvisited[ind].y - self.allVehicles[
                                             vind].y, 2))
                        dist1 = math.sqrt(math.pow(self.startx - self.allVehicles[vind].x, 2) +
                                          math.pow(self.starty - self.allVehicles[
                                              vind].y, 2))  # distance of the next node to the depot
                        bigvar = self.allVehicles[vind].t + self.unvisited[ind].st + dist + dist1
                        if self.unvisited[ind].d <= self.allVehicles[vind].q and bigvar <= self.timecon:
                            self.allVehicles[vind].t += self.unvisited[ind].st + dist
                            self.allVehicles[vind].x = self.unvisited[ind].x
                            self.allVehicles[vind].y = self.unvisited[ind].y
                            self.allVehicles[vind].q -= self.unvisited[ind].d
                            self.total_profit += self.unvisited[ind].p
                            self.visited.append(self.unvisited[ind])
                            self.dict[vind] = self.visited  # sos
                            self.unvisited.pop(
                                ind)  # remove the element from the unvisited list (This may need to be done later)
                            unvisited_length = len(self.unvisited)
                            reprint = 0
                        else:
                            self.print_route(self.allVehicles[vind].id)
                            # self.allVehicles.pop(vind)
                            bool = False
                            reprint = -1
                            self.visited.clear()
                        vehicles_length = len(self.allVehicles)
                        mp = -1
            if reprint == 0:
                self.print_route(self.allVehicles[vind].id)
                self.visited.clear()
            print('Total Profit')
        return self.total_profit

    def distance(self, x1, y1, x2, y2):
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return d

    def print_route(self, v1):
        print('Route', v1)
        print(self.customers[0].ID, end=" ")
        if (v1 - 1 in self.dict.keys()):
            tempList = self.dict[v1 - 1]
            for item in tempList:
                print(item.ID, end=" ")
        print(self.customers[0].ID)

    def BuildModel(self, n, k, Q, T, xdep, ydep):
        random.seed(10)
        depot = Customer(0, xdep, ydep, 0, 0, 0)
        self.customers.append(depot)

        totalCustomers = n
        totalVehicles = k
        self.startx = xdep
        self.starty = ydep

        for i in range(0, totalVehicles):
            veh = Vehicles(i + 1, xdep, ydep, Q, 0)
            self.allVehicles.append(veh)

        self.timecon = T

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
m.BuildModel(5, 3, 250, 300, 23.142, 11.736)
print(m.max_profit())
print('test')
