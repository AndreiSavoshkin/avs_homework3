import random
import vehicle


# ----------------------------------------------

class Bus(vehicle.Vehicle):
    def __init__(self):
        super().__init__()
        self.passengersCapacity = 0

    def ReadStrArray(self, strArray, i):
        if i >= len(strArray) - 1:
            return 0
        self.fuelCapacity = int(strArray[i])
        self.fuelConsumption = int(strArray[i + 1])
        self.passengersCapacity = float(strArray[i + 2])
        i += 3
        return i

    def InRnd(self):
        self.passengersCapacity = random.randint(1, 20) + 1

    def Print(self):
        print("Bus: passengersCapacity = ", self.passengersCapacity, ", fuelCapacity = ", self.fuelCapacity,
              ", fuelConsumption = ", self.fuelConsumption, "Distance = ", self.Distance())
        pass

    def Write(self, fileToWrite):
        fileToWrite.write("Bus: passengersCapacity = {}, fuelCapacity = {}, fuelConsumption = {}, Distance = {}"
                          .format(self.passengersCapacity, self.fuelCapacity, self.fuelConsumption, self.Distance()))
        pass

    def Distance(self):
        return self.fuelCapacity / self.fuelConsumption * 100
        pass
