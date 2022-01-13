import math
import operator

f = open("sol.txt", "w+")


class Model:
    # instance variables
    def __init__(self):
        self.allVehicles = []
        self.visited = []
        self.unvisited = []
        self.customers = []
        self.matrix = {}
        self.total_profit = 0
        self.timecon = 0
        self.dict = {}
        self.sorted_d = {}

    def max_profit(self):
        unvisited_length = len(self.unvisited)
        vehicles_length = len(self.allVehicles)
        print('Total Profit', file=f)
        for vindex in range(0, vehicles_length):
            if self.allVehicles[vindex].q > 0 and self.allVehicles[vindex].t < self.timecon:
                vind = vindex
                if unvisited_length > 0:
                    state = True
                while state:
                    condition = False
                    self.sorted_d = self.create_dict(self.unvisited, vind)
                    for key in self.sorted_d:
                        if condition:
                            break
                        for u in range(0, unvisited_length):  # find the customer who has his ID = key
                            if key == self.unvisited[u].ID:  # key = ID of the customer
                                dist = m.distance(self.allVehicles[vind].x, self.allVehicles[
                                    vind].y, self.unvisited[u].x, self.unvisited[u].y)
                                # distance of our current spot to the next customer
                                dist2 = m.distance(self.unvisited[u].x, self.unvisited[
                                    u].y, self.startx, self.starty)
                                # distance of the next customer to the depot
                                bigvar = self.allVehicles[vind].t + self.unvisited[u].st + dist + dist2
                                if self.allVehicles[vind].q > 0 and bigvar <= self.timecon and \
                                        self.customers[
                                            u].ID != 0:
                                    # we change the dictionaries cause the vehicle moves
                                    condition = True
                                    self.allVehicles[vind].t += self.unvisited[u].st + dist
                                    self.allVehicles[vind].x = self.unvisited[u].x
                                    self.allVehicles[vind].y = self.unvisited[u].y
                                    if self.allVehicles[vind].q >= self.unvisited[u].d:
                                        self.allVehicles[vind].q -= self.unvisited[u].d
                                        self.total_profit += self.unvisited[u].p
                                        self.visited.append(self.unvisited[u])
                                        self.dict[vind] = self.visited.copy()
                                        self.unvisited.pop(
                                            u)  # remove the element from the unvisited list
                                        unvisited_length = len(self.unvisited)
                                        if self.allVehicles[vind].q == 0:
                                            state = False
                                        break
                                    else:
                                        self.unvisited[u].d -= self.allVehicles[vind].q
                                        self.allVehicles[vind].q = 0
                                        self.visited.clear()
                                        unvisited_length = len(self.unvisited)
                                        state = False
                                        # We change the dictionaries
                                        break
                                else:
                                    break
                    if not condition:
                        state = False
                        self.visited.clear()
        return self.total_profit, self.dict

    def distance(self, x1, y1, x2, y2):
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return d

    def print_route(self, dictrts):
        temp_dict = dictrts
        for key in temp_dict.keys():
            print('Route', key + 1, end="\n", file=f)
            print(self.customers[0].ID, end=" ", file=f)
            temp_list = temp_dict[key]
            for item in temp_list:
                print(item.ID, end=" ", file=f)
            print(self.customers[0].ID, end='\n', file=f)

    def create_dict(self, unv_list, vindd):
        unvisited_length = len(unv_list)
        vind = vindd
        self.matrix.clear()
        for index in range(0, unvisited_length):
            dist0 = m.distance(self.allVehicles[vind].x,
                               self.allVehicles[vind].y, self.unvisited[index].x,
                               self.unvisited[index].y)
            # distance of our current spot to the next customer
            dist1 = m.distance(self.unvisited[index].x, self.unvisited[
                index].y, self.startx, self.starty)
            # dist of the next customer to the depot
            self.matrix[self.unvisited[index].ID] = (
                    self.unvisited[index].p / (self.unvisited[index].st + dist0 + dist1))
            # dict that keeps the ID of the customer and its actual profit(profit/dist0)
            tempdict = dict(
                sorted(self.matrix.items(), key=operator.itemgetter(1), reverse=True))
            # we sort the above dict by descending values so its worth to go to the first one
            ind = list(tempdict.keys())[0]
            # the id of the first customer of the list
        return tempdict

    def BuildModel(self, n, k, Q, T, xdep, ydep):
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

        from csv import reader
        # skip first line i.e. read header first and then iterate over each row od csv as a list
        with open('C://Users//dimpa//Documents//csvfile.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            # Check file as empty
            if header != None:
                # Iterate over each row after the header in the csv
                for row in csv_reader:
                    # row variable is a list that represents a row in csv
                    id1 = int(row[0])
                    x = float(row[1])
                    y = float(row[2])
                    d = int(row[3])
                    st = int(row[4])
                    p = int(row[5])
                    cust = Customer(id1, x, y, d, st, p)
                    self.customers.append(cust)
                    self.unvisited.append(cust)


class Customer:
    def __init__(self, idd, xx, yy, dd, stt, pp):
        self.x = xx
        self.y = yy
        self.ID = idd
        self.d = dd
        self.st = stt
        self.p = pp


class Vehicles:
    def __init__(self, iddd, xxx, yyy, qqq, ttt):
        self.id = iddd
        self.x = xxx
        self.y = yyy
        self.q = qqq
        self.t = ttt


m = Model()
m.BuildModel(336, 6, 150, 200, 23.142, 11.736)
f = open("sol.txt", "w+")
tup = m.max_profit()
tot_profit = tup[0]
dictroutes = tup[1]
print(tot_profit, file=f)
m.print_route(dictroutes)
f.close()
