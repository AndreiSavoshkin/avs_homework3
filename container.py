# ----------------------------------------------
import random

import bus
import car
import truck
import vehicle


class Container:
    def __init__(self):
        self.store = []
        self.length = 0

    def InRnd(self, size):
        while self.length < size:
            vh = self.InVhRnd()
            self.store.append(vh)
            self.length += 1

    def Print(self):
        print("Container is store", len(self.store), "vehicles:")
        for veh in self.store:
            veh.Print()
        print("Average of Distances  = ", self.averageDistance())
        pass

    def Write(self, fileName):
        fileName.write("Container is store {} vehicles:\n".format(len(self.store)))
        for veh in self.store:
            veh.Write(fileName)
            fileName.write("\n")
        fileName.write("Average of Distances  =  {}\n".format(self.averageDistance()))
        pass

    def averageDistance(self):
        sumDistance = 0.0
        counter = 0
        for veh in self.store:
            sumDistance += veh.Distance()
            counter += 1
        return sumDistance / counter

    def moveAutos(self):
        averDistance = self.averageDistance()
        for i in range(len(self.store)):
            if self.store[i].Distance() < averDistance:
                self.store.append(self.store.pop(i))

    @staticmethod
    def InVhRnd():
        k = random.randrange(1, 4)
        vh = vehicle.Vehicle()
        if k == 1:
            vh = bus.Bus()
        elif k == 2:
            vh = car.Car()
        elif k == 3:
            vh = truck.Truck()
        vh.InRnd()
        vh.fuelCapacity = 45 + random.randint(1, 20)
        vh.fuelConsumption = 2.5 - (random.randint(1, 20) % 15) / 10.0
        return vh
