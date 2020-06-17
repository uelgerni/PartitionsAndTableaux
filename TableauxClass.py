from Sliding import *

arr = np.ndarray

"""
basic tableaux class for multiplication
"""


class Tableaux(arr):

    def __new__(cls, input_array):
        # print('In __new__ with class %s' % cls)
        obj = np.asarray(input_array).view(cls)
        return obj

    def __array_finalize__(self, obj):
        # see InfoArray.__array_finalize__ for comments
        if obj is None: return
        self.info = getattr(obj, 'info', None)

    def __mul__(self, other):  # carries out Multiplication of tableaux using the sliding operation

        # a = [self]
        # b[i] =
        c = (-1) * np.ones((len(other), len(self.T)))
        d = np.zeros((len(self), len(other.T)))
        e = np.concatenate((np.concatenate((c, other), axis=1), np.concatenate((self, d), axis=1)),
                           axis=0)  # constructs skewtableau from a and b as explaint in W.Fultons book
        stableau = np.concatenate((np.concatenate((e, np.zeros((len(e), 2))), axis=1), np.zeros((2, len(e.T) + 2))),
                                  axis=0)  # adds two rows and columns of zeros to avoid indexerror in sliding
        while stableau[0][0] == -1:  # does sliding operation until the result is a youngtableau
            stableau = np.copy(Sliding(stableau))
        stableau = np.delete(stableau, (-1), axis=1)
        stableau = np.delete(stableau, (-1), axis=0)
        stableau = np.delete(stableau, (-1), axis=1)
        stableau = np.delete(stableau, (-1), axis=0)  # deletes rows and columns of zeros
        return stableau



a = Tableaux([[1, 5, 3,5]])
b = Tableaux(([[1], [4], [3]]))
c = a * b
print(c)
