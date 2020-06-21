import numpy as np

def rowinsertion(tableau,newentry):         #carries out row insertion operation as defined in W. Fultons book, if the matrix reprsesntion of the tableau has enough rows and columns
    k=0
    for i in range(len(tableau)):
        for j in range(len(tableau.T)):
            if tableau [i][j]>newentry:
                tableau[i][j],newentry=newentry,tableau[i][j]
                break
        else:
            for j in range(len(tableau.T)):
                if tableau[i][j] == 0 :
                    tableau[i][j]=newentry
                    k=1
                    break
        if k==1:
            break
    return (tableau,(i,j))


def deleteemptyrows(tableau):           #deletes every row in a matrix that only has zeros in it
    k=0
    for i in range(len(tableau)):
        for j in range(len(tableau.T)):
            if tableau[i-k][j]!=0:
                break
        else:
            tableau = np.delete(tableau, (i-k), axis=0)
            k=k+1
    return tableau


def deleteemptycols(tableau):           #deletes every column in a matrix that only has zeros in it
    k=0
    for j in range(len(tableau.T)):
        for i in range(len(tableau)):
            if tableau[i][j-k]!=0:
                break
        else:
            tableau = np.delete(tableau, (j-k), axis=1)
            k=k+1
    return tableau

def saverowinsertion(tableau,newentry):         #does rowinsertion for every tableau using rowinsertion function and deletes empty rows and columns
    tableau = np.concatenate((np.concatenate((tableau,np.zeros((len(tableau),1))),axis=1),np.zeros((1,len(tableau.T)+1))),axis=0)
    (tableau,newbox) = rowinsertion(tableau,newentry)
    tableau = deleteemptyrows(tableau)
    tableau = deleteemptycols(tableau)
    return tableau,newbox



#t = np.array([[1,2,3,0,0,0],[2,3,4,0,0,0],[3,4,5,0,0,0],[0,0,0,0,0,0,],[0,0,0,0,0,0,],[0,0,0,0,0,0,],[0,0,0,0,0,0,]])

#print(saverowinsertion(t,2)[0])


