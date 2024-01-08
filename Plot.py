import matplotlib.pyplot as plt
from Cluster import Cluster
from DimensionReduction import ReduceDimensions
import random


def RandomNumbers(count):
    tmp = []
    for e in range(count):
        tmp.append(random.randrange(0, 50001))
    return tmp



def PlotClusters(docNums):

    tmp = ReduceDimensions(docNums)
    tmp2 = Cluster(tmp, 5)

    for i in range(len(docNums)):
        if tmp2[i] == 0:
            plt.plot(tmp[i][0], tmp[i][1], 'or')
        elif tmp2[i] == 1:
            plt.plot(tmp[i][0], tmp[i][1], 'ob')
        elif tmp2[i] == 2:
            plt.plot(tmp[i][0], tmp[i][1], 'og')
        elif tmp2[i] == 3:
            plt.plot(tmp[i][0], tmp[i][1], 'oy')
        else:
            plt.plot(tmp[i][0], tmp[i][1], 'ok')

    plt.show()
    return 1



def RandomPlot(countOfRandNumbers=1000):
    PlotClusters(RandomNumbers(countOfRandNumbers))
    return 1




RandomPlot()