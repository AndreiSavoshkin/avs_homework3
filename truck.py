import vehicle
import random


# ----------------------------------------------

class Truck(vehicle.Vehicle):
    def __init__(self):
        super().__init__()
        self.loadCapacity = 0

    def ReadStrArray(self, strArray, i):
        if i >= len(strArray) - 1:
            return 0
        self.fuelCapacity = int(strArray[i])
        self.fuelConsumption = int(strArray[i + 1])
        self.loadCapacity = float(strArray[i + 2])
        i += 3
        return i

    def InRnd(self):
        self.loadCapacity = random.randint(1, 10) + 1

    def Print(self):
        print("Truck: loadCapacity = ", self.loadCapacity, ", fuelCapacity = ", self.fuelCapacity,
              ", fuelConsumption = ", self.fuelConsumption, "Distance = ", self.Distance())
        pass

    def Write(self, fileToWrite):
        fileToWrite.write("Truck: loadCapacity = {}, fuelCapacity = {}, fuelConsumption = {}, Distance = {}"
                          .format(self.loadCapacity, self.fuelCapacity, self.fuelConsumption, self.Distance()))
        pass

    def Distance(self):
        return self.fuelCapacity / self.fuelConsumption * 100
        pass
