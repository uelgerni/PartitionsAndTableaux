import numpy as np

arr = np.ndarray

"""
basic tableaux class for multiplication with *
includes all the basic operations needed

where needed those functions now also have a cast to tableaux inside
"""


class Tableaux(arr):

    def __new__(cls, input_array):  # creating an ndarray from a list or similar object and casting it to Tableaux type
        obj = np.asarray(input_array).view(cls)
        return obj

    def sliding(self):  # does the basic operation Sliding of a skewtableau
        stableau = self
        for i in range(len(stableau)):
            for j in range(len(stableau.T)):
                if stableau[i][j] == -1:
                    if i == len(stableau) or stableau[i + 1][j] != -1:
                        if j == len(stableau.T) or stableau[i][j + 1] != -1:  # identifies inside corner of skewtableau
                            while True:  # moves the corner according to sliding operation until it is on the outside, then gives it value 0
                                if stableau[i + 1][j] <= stableau[i][j + 1] and stableau[i + 1][j] != 0:
                                    stableau[i][j] = stableau[i + 1][j]
                                    stableau[i + 1][j] = -1
                                    i = i + 1
                                    if stableau[i + 1][j] == 0 or i == len(stableau):
                                        if stableau[i][j + 1] == 0 or j == len(stableau.T):
                                            stableau[i][j] = 0
                                            break
                                elif stableau[i][j + 1] == 0:
                                    stableau[i][j] = stableau[i + 1][j]
                                    stableau[i + 1][j] = -1
                                    i = i + 1
                                    if stableau[i + 1][j] == 0 or i == len(stableau):
                                        if stableau[i][j + 1] == 0 or j == len(stableau.T):
                                            stableau[i][j] = 0
                                            break
                                else:
                                    stableau[i][j] = stableau[i][j + 1]
                                    stableau[i][j + 1] = -1
                                    j = j + 1
                                    if stableau[i + 1][j] == 0 or i == len(stableau):
                                        if stableau[i][j + 1] == 0 or j == len(stableau.T):
                                            stableau[i][j] = 0
                                            break
                            stableau = stableau.view(Tableaux)
                            return stableau

    def savesliding(self):
        if self[0][0] != -1:
            return self
        result = np.concatenate(
            (np.concatenate((self, np.zeros((len(self), 2))), axis=1), np.zeros((2, len(self.T) + 2))), axis=0)
        result = result.view(Tableaux)
        result = result.sliding()
        result = result.deleteemptyrows()
        result = result.deleteemptycols()
        return result

    def rowinsertion(self,newentry):
        # carries out row insertion operation as defined in W. Fultons book, iff the matrix reprsesntion of the tableau has enough rows and columns
        # so better use saverowinsertion
        tableau = self
        k = 0
        for i in range(len(tableau)):
            for j in range(len(tableau.T)):
                if tableau[i][j] > newentry:
                    tableau[i][j], newentry = newentry, tableau[i][j]
                    break
            else:
                for j in range(len(tableau.T)):
                    if tableau[i][j] == 0:
                        tableau[i][j] = newentry
                        k = 1
                        break
            if k == 1:
                break
        tableau = tableau.view(Tableaux)
        return tableau, (i, j)

    def deleteemptyrows(self):  # deletes every row in a matrix that only has zeros in it
        tableau = self
        k = 0
        for i in range(len(tableau)):
            for j in range(len(tableau.T)):
                if tableau[i - k][j] != 0:
                    break
            else:
                tableau = np.delete(tableau, (i - k), axis=0)
                k = k + 1
        tableau = tableau.view(Tableaux)
        return tableau

    def deleteemptycols(self):  # deletes every column in a matrix that only has zeros in it
        tableau = self
        k = 0
        for j in range(len(tableau.T)):
            for i in range(len(tableau)):
                if tableau[i][j - k] != 0:
                    break
            else:
                tableau = np.delete(tableau, (j - k), axis=1)
                k = k + 1
        tableau = tableau.view(Tableaux)
        return tableau

    def saverowinsertion(self, newentry):  # does rowinsertion for every tableau using rowinsertion function and deletes empty rows and columns
        tableau = self
        tableau = np.concatenate((np.concatenate((tableau, np.zeros((len(tableau), 1))), axis=1), np.zeros((1, len(tableau.T) + 1))), axis=0)
        tableau = tableau.view(Tableaux)
        (tableau, newbox) = tableau.rowinsertion(newentry)
        tableau = tableau.deleteemptyrows()
        tableau = tableau.deleteemptycols()
        return tableau, newbox

    def __mul__(self, other):  # carries out Multiplication of tableaux using the sliding operation

        c = (-1) * np.ones((len(other), len(self.T)))
        d = np.zeros((len(self), len(other.T)))
        e = np.concatenate((np.concatenate((c, other), axis=1), np.concatenate((self, d), axis=1)), axis=0)  # constructs skewtableau from a and b as explaint in W.Fultons book
        stableau = np.concatenate((np.concatenate((e, np.zeros((len(e), 2))), axis=1), np.zeros((2, len(e.T) + 2))), axis=0)  # adds two rows and columns of zeros to avoid indexerror in sliding
        stableau = stableau.view(Tableaux)
        while stableau[0][0] == -1:  # does sliding operation until the result is a youngtableau
            stableau = Tableaux.copy(stableau.sliding())
        stableau = stableau.deleteemptyrows()
        stableau = stableau.deleteemptycols()  # deletes rows and columns of zeros
        return stableau


#a = Tableaux([[1, 3, 3, 5], [1, 2, 0, 0]])
#r = Tableaux([[-1, -1, 3, 4], [1, 2, 0, 0]])
#b = Tableaux([[1, 2, 3]])
#c = a * b
#print(c)

#d = c.saverowinsertion(3)
#d= r.savesliding()
#print(d)
