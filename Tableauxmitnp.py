import numpy as np
from TableauxClass import Tableaux


def TableauxGenerator(diagram, max, liste=[(0, 0)], next=2):                #recursive generator that gives all tableaux corresponding to a Young diagram, needs number of boxes in diagram as max
    diagram[0][0] = 1

    if next > max:
        yield diagram
    else:
        for i in range(len(diagram)):
            for j in range(len(diagram[i])):
                if diagram[i][j] == -1 and (i, j) not in liste:
                    if (i, j - 1) in liste or j == 0:
                        if (i - 1, j) in liste or i == 0:
                            a = np.copy(diagram)  # to create deepcopy
                            a[i][j] = next
                            for k in TableauxGenerator(a, max, liste + [(i, j)], next + 1):
                                yield k


def diagramprep(d):                                                                                                  #prepares diagram for TableauxGenerator
    diagram = np.concatenate((np.concatenate((d,np.zeros((len(d),2))),axis=1),np.zeros((2,len(d.T)+2))),axis=0)     #adds rows and columns with zeros
    max = (-1)*np.sum(diagram)                                                                                      #calculates max (number of boxes)
    return (diagram,max)

def diagramm(partition):    #returns Youngdiagram corresponding to partition
    a = len(partition)
    b = partition[0]

    diagram = np.zeros((a, b))
    for x in range(a):
        for y in range(partition[x]):
            diagram[x][y] = -1
    return diagram


def tableaux(p):        #generator that yields all the tableaux corresponding to a Partition
    d = diagramm(p)
    diagram=diagramprep(d)
    for p in TableauxGenerator(diagram[0], diagram[1]):
        p = np.delete(p, (-1), axis=1)              #deletes columns and rows with zeros
        p = np.delete(p, (-1), axis=0)
        p = np.delete(p, (-1), axis=1)
        p = np.delete(p, (-1), axis=0)
        p.tolist()
        p = Tableaux(p)
        yield(p)



p=(4, 2, 1, 1)


diagram = np.array([[-1, -1 ], [-1, 0 ]])

for i in tableaux(p):
    print(i)