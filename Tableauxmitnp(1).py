import numpy as np


def TableauxGenerator(diagram, max, liste=[(0, 0)], next=2):
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


def tableaux(d):
    diagram = np.concatenate((np.concatenate((d,np.zeros((len(d),2))),axis=1),np.zeros((2,len(d.T)+2))),axis=0)     #add rows and columns with zeros
    max = (-1)*np.sum(diagram)
    return diagram,max




diagram = np.array([[-1, -1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

for p in TableauxGenerator(diagram,3):
    print(p)
