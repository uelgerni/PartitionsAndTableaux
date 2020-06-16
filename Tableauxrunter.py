import numpy as np

def outsidecorners(diagram):
    for i in range(len(diagram)):
        for j in range(len(diagram.T)):
            if diagram[i][j] == -1:
                if diagram[i][j + 1] != -1:
                    if diagram[i + 1][j] != -1:
                        yield (i,j)

def TableauxGenerator(diagram,max):
    if max==1:
        diagram[0,0]=1
        yield diagram
    else:
        for i in outsidecorners(diagram):
            a = np.copy(diagram)
            a[i[0],i[1]]=max
            for k in  TableauxGenerator(a,max-1):
                yield k


diagram= np.array([[-1,-1,-1,0],[-1,-1,-1,0],[0,0,0,0],[0,0,0,0]])

for p in TableauxGenerator(diagram,6):
    print(p)





