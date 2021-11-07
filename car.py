import vehicle
import random


# ----------------------------------------------

class Car(vehicle.Vehicle):
    def __init__(self):
        super().__init__()
        self.maxSpeed = 0

    def InRnd(self):
        self.maxSpeed = random.randint(1, 100) + 90

    def ReadStrArray(self, strArray, i):
        if i >= len(strArray) - 1:
            return 0
        self.fuelCapacity = int(strArray[i])
        self.fuelConsumption = float(strArray[i + 1])
        self.maxSpeed = float(strArray[i + 2])
        i += 3
        return i

    def Print(self):
        print("Car: maxSpeed = ", self.maxSpeed, ", fuelCapacity = ", self.fuelCapacity,
              ", fuelConsumption = ", self.fuelConsumption, "Distance = ", self.Distance())
        pass

    def Write(self, fileToWrite):
        distance = self.Distance()
        fileToWrite.write("Car: maxSpeed = {}, fuelCapacity = {}, fuelConsumption = {}, Distance = {}"
                          .format(self.maxSpeed, self.fuelCapacity, self.fuelConsumption, distance))
        pass

    def Distance(self):
        return self.fuelCapacity / self.fuelConsumption * 100
