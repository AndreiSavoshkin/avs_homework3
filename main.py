import sys
import time
import container

# ----------------------------------------------
from readStrArray import ReadStrArray

if __name__ == '__main__':
    beginTime = time.perf_counter()
    if len(sys.argv) == 3:
        inputFileName = sys.argv[1]
        outputFileName = sys.argv[2]
    elif len(sys.argv) == 2:
        inputFileName = sys.argv[1]
        outputFileName = "output.txt"
    elif len(sys.argv) == 1:
        print("Incorrect command line! You must write: python main <inputFileName> [<outputFileName>]\n")
        print("                                        python main [<amount of random number>] [<outputFileName>]")
        exit()

    container = container.Container()

    if not (inputFileName.isdigit()):
        file = open(inputFileName)
        strInput = file.read()
        file.close()

        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        strArray = strInput.replace("\n", " ").split(" ")
        figNum = ReadStrArray(container, strArray)
    else:
        container.InRnd(int(inputFileName))

    outputFile = open(outputFileName, 'w')
    container.Write(outputFile)
    container.moveAutos()
    outputFile = open(outputFileName.replace(".txt", "_sorted.txt"), 'w')
    container.Write(outputFile)
    outputFile.close()
    endTime = time.perf_counter()
    print("Time: {}".format(endTime - beginTime))
