import numpy as np




def diagramm(partition):        #returns the young diagram correspnding to given partition
    a = len(partition)
    b = partition[0]

    diagram = np.zeros((a, b))
    for x in range(a):
        for y in range(partition[x]):
            diagram[x][y] = 1
    return (-1)*diagram




print (diagramm((3, 1, 1)))

