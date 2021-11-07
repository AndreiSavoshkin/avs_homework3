import truck
import car
import bus


def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0  # Индекс, задающий текущую строку в массиве
    figNum = 0
    while i < arrayLen:
        inputString = strArray[i]
        key = int(inputString)  # преобразование в целое
        if key == 1:
            i += 1
            vehicle = bus.Bus()
            i = vehicle.ReadStrArray(strArray, i)
        elif key == 2:
            i += 1
            vehicle = car.Car()
            i = vehicle.ReadStrArray(strArray, i)
        elif key == 3:
            i += 1
            vehicle = truck.Truck()
            i = vehicle.ReadStrArray(strArray, i)
        else:
            return figNum
        if i == 0:
            return figNum
        figNum += 1
        container.store.append(vehicle)
    return figNum
