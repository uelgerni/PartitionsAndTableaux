import numpy as np  # alternative way to construct young tableaux (recursion is done in the other direction)
from TableauxClass import Tableaux


def outsidecorners(diagram):  # calculates all outsidecorners of a young tableau, or skew tableau
    for i in range(len(diagram)):
        for j in range(len(diagram.T)):
            if diagram[i][j] == -1:
                if diagram[i][j + 1] != -1:
                    if diagram[i + 1][j] != -1:
                        yield (i, j)


def TableauxGenerator(diagram,
                      max):  # recursiv generator that yields all tableaux corresponding to a diagram, needs to be given number of boxes as max
    if max == 1:
        diagram[0, 0] = 1
        yield diagram
    else:
        for i in outsidecorners(diagram):
            a = np.copy(diagram)
            a[i[0], i[1]] = max
            for k in TableauxGenerator(a, max - 1):
                yield k


def diagramprep(d):  # prepares diagram for TableauxGenerator
    diagram = np.concatenate((np.concatenate((d, np.zeros((len(d), 2))), axis=1), np.zeros((2, len(d.T) + 2))),
                             axis=0)  # adds rows and columns with zeros
    max = (-1) * np.sum(diagram)  # calculates max (number of boxes)
    return (diagram, max)


def diagramm(partition):  # returns Youngdiagram corresponding to partition
    a = len(partition)
    b = partition[0]

    diagram = np.zeros((a, b))
    for x in range(a):
        for y in range(partition[x]):
            diagram[x][y] = -1
    return diagram


def tableaux(p):  # generator that yields all the tableaux corresponding to a Partition
    d = diagramm(p)
    diagram = diagramprep(d)
    for p in TableauxGenerator(diagram[0], diagram[1]):
        p = np.delete(p, (-1), axis=1)  # deletes columns and rows with zeros
        p = np.delete(p, (-1), axis=0)
        p = np.delete(p, (-1), axis=1)
        p = np.delete(p, (-1), axis=0)
        p.tolist()
        p = Tableaux(p)
        yield (p)


p = (4, 2, 1, 1)

diagram = np.array([[-1, -1], [-1, 0]])

for i in tableaux(p):
    print(i)
