from rowinsertion import *
from TableauxClass import *

def SchenstedAlgorithm(S):                  #Schensted algorithm as explaint in Wikipedia article "Robinson-Schensted correspondence"
    a=np.array([[]])
    b=np.array([[]])
    k=1
    for i in S:
        b= np.concatenate((np.concatenate((b,np.zeros((len(b),1))),axis=1),np.zeros((1,len(b.T)+1))),axis=0)
        a,n=saverowinsertion(a,int(i))
        b[n[0]][n[1]]=k
        b = deleteemptycols(b)
        b = deleteemptyrows(b)
        k=k+1
    a.tolist()
    b.tolist()
    a = Tableaux(a)
    b = Tableaux(b)
    return [a,b]



r= SchenstedAlgorithm([1,6,3,4,2,7,5])
print ("insertion tableau:")
print (r[0])
print ("recording tableau:")
print (r[1])



