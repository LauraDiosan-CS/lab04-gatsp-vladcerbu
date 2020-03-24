from GA import *
from Repository import *


def startzero(repres):
    while repres[0] != 0:
        repres.insert(0, repres.pop())
    return repres


def doga(pop, iter, path1, path2):
    param = {"popSize": pop, "noGen": iter}
    problParam = readnet(path1)
    problParam["function"] = modularity
    test = GA(param, problParam)
    test.initialisation()
    for i in range(param["noGen"]):
        test.oneGenerationElitism()
        print(test.bestChromosome())
        print("Gen", i+1, "\n")
    rez = test.bestChromosome()
    rez.repres = startzero(rez.repres)
    writerez(rez, path2)
    return rez


def modularity(repres, matrix):
    Q = 0.0
    for i in range(len(repres) - 1):
        Q += matrix[repres[i]][repres[i+1]]
    return Q + matrix[repres[len(repres) - 1]][repres[0]]
