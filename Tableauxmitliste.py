import numpy as np


def TableauxGenerator(diagram, max, liste=[(0, 0)], next=2):    #alternative way to find young tableaux to diagram, uses lists instead of ndarrays
    diagram[0][0] = 1                                            #this takes less space in the output window, but everything alse is done with nparrays and the output is a little harder to read
                                                                # also needs to be given number of boxes
    if next > max:
        yield diagram
    else:
        for i in range(len(diagram)):
            for j in range(len(diagram[i])):
                if diagram[i][j] == -1 and (i, j) not in liste:
                    if (i, j - 1) in liste or j == 0:
                        if (i - 1, j) in liste or i == 0:
                            a = [x[:] for x in diagram]  # to create deepcopy
                            a[i][j] = next
                            for k in TableauxGenerator(a, max, liste + [(i, j)], next + 1):
                                yield k





diagram = [[-1, -1, -1, -1], [-1, -1, -1, 0], [-1, -1, 0, 0], [0, 0, 0, 0]]

for p in TableauxGenerator(diagram, 9):
    print(p)
