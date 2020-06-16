import numpy as np
from Sliding import *

def mult(a,b):
    c = (-1) * np.ones((len(b), len(a.T)))
    d = np.zeros((len(a), len(b.T)))
    e = np.concatenate((np.concatenate((c,b),axis=1),np.concatenate((a, d), axis=1)),axis=0)
    stableau = np.concatenate((np.concatenate((e,np.zeros((len(e),2))),axis=1),np.zeros((2,len(e.T)+2))),axis=0)
    while stableau[0][0]== -1:
        stableau=np.copy(Sliding(stableau))
    stableau= np.delete(stableau,(-1),axis=1)
    stableau = np.delete(stableau, (-1), axis=0)
    return stableau


a = np.array([[1,2,3]])
b = np.array(([[1],[2],[3]]))

c=mult(a,b)
print (c)
