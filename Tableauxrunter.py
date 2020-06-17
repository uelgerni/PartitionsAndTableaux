import numpy as np                              #alternative way to construct young tableaux (recursion is done in the other direction)

def outsidecorners(diagram):                    #calculates all outsidecorners of a young tableau, or skew tableau
    for i in range(len(diagram)):
        for j in range(len(diagram.T)):
            if diagram[i][j] == -1:
                if diagram[i][j + 1] != -1:
                    if diagram[i + 1][j] != -1:
                        yield (i,j)

def TableauxGenerator(diagram,max):             #recursiv generator that yields all tableaux corresponding to a diagram, needs to be given number of boxes as max
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





