import numpy as np
from Sliding import *

def mult(a,b):          #carries out Multiplication of tableaux using the sliding operation
    c = (-1) * np.ones((len(b), len(a.T)))
    d = np.zeros((len(a), len(b.T)))
    e = np.concatenate((np.concatenate((c,b),axis=1),np.concatenate((a, d), axis=1)),axis=0)                         #constructs skewtableau from a and b as explaint in W.Fultons book
    stableau = np.concatenate((np.concatenate((e,np.zeros((len(e),2))),axis=1),np.zeros((2,len(e.T)+2))),axis=0)    #adds two rows and columns of zeros to avoid indexerror in sliding
    while stableau[0][0]== -1:                  #does sliding operation until the result is a youngtableau
        stableau=np.copy(Sliding(stableau))
    stableau= np.delete(stableau,(-1),axis=1)
    stableau = np.delete(stableau, (-1), axis=0)
    stableau= np.delete(stableau,(-1),axis=1)
    stableau = np.delete(stableau, (-1), axis=0)            #deletes rows and columns of zeros
    return stableau


a = np.array([[1,5,3,5]])
b = np.array(([[1,4,3]]))

c=mult(a,b)
print (c)



