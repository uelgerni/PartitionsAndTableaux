from Sliding import *

class Tableaux():

    def TableauxGenerator(self, diagram, max, liste=[(0, 0)], next=2):
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
                                for k in self.TableauxGenerator(a, max, liste + [(i, j)], next + 1):
                                    yield k

    def diegramprep(self, d):
        diagram = np.concatenate((np.concatenate((d, np.zeros((len(d), 2))), axis=1), np.zeros((2, len(d.T) + 2))),
                                 axis=0)  # add rows and columns with zeros
        max = (-1) * np.sum(diagram)
        return (diagram, max)

    def __init__(self, d):
        diagram = self.diegramprep(d)
        for p in self.TableauxGenerator(diagram[0], diagram[1]):
            p = np.delete(p, (-1), axis=1)
            p = np.delete(p, (-1), axis=0)
            p = np.delete(p, (-1), axis=1)
            p = np.delete(p, (-1), axis=0)
            print(p)

    def __mul__(self, other):
        c = (-1) * np.ones((len(other), len(self.T)))
        d = np.zeros((len(self), len(other.T)))
        e = np.concatenate((np.concatenate((c, other), axis=1), np.concatenate((self, d), axis=1)), axis=0)
        stableau = np.concatenate((np.concatenate((e, np.zeros((len(e), 2))), axis=1), np.zeros((2, len(e.T) + 2))),
                                  axis=0)
        while stableau[0][0] == -1:
            stableau = np.copy(Sliding(stableau))
        stableau = np.delete(stableau, (-1), axis=1)
        stableau = np.delete(stableau, (-1), axis=0)
        return stableau

    def mult(a, b):
        c = (-1) * np.ones((len(b), len(a.T)))
        d = np.zeros((len(a), len(b.T)))
        e = np.concatenate((np.concatenate((c, b), axis=1), np.concatenate((a, d), axis=1)), axis=0)
        stableau = np.concatenate((np.concatenate((e, np.zeros((len(e), 2))), axis=1), np.zeros((2, len(e.T) + 2))),
                                  axis=0)
        while stableau[0][0] == -1:
            stableau = np.copy(Sliding(stableau))
        stableau = np.delete(stableau, (-1), axis=1)
        stableau = np.delete(stableau, (-1), axis=0)
        return stableau

a = np.array([[1,2,3]])
b = np.array(([[1],[2],[3]]))

c= a * b
print (c)

c = a.mult(b)