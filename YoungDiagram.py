import numpy as np




def diagramm(partition):
    a = len(partition)
    b = partition[0]

    diagram = np.zeros((a, b))
    for x in range(a):
        for y in range(partition[x]):
            diagram[x][y] = 1
    return diagram




print (diagramm((3, 1, 1)))

