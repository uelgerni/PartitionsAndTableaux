import numpy as np

def Sliding(stableau):                      #does the basic operation Sliding of a skewtableau
    for i in range(len(stableau)):
        for j in range(len(stableau.T)):
            if stableau[i][j]==-1:
                if i == len(stableau) or stableau[i+1][j]!=-1 :
                    if j == len(stableau.T) or stableau[i][j+1]!=-1 :           #identifies inside corner of skewtableau
                        while True:                                             #moves the corner according to sliding operation until it is on the outside
                            if stableau[i+1][j]<=stableau[i][j+1] and stableau[i+1][j]!=0:
                                stableau[i][j]=stableau[i+1][j]
                                stableau[i+1][j]=-1
                                i = i+1
                                if stableau[i + 1][j] == 0 or i == len(stableau):
                                    if stableau[i][j + 1] == 0 or j == len(stableau.T):
                                        stableau[i][j]=0
                                        break
                            elif stableau[i][j+1]==0:
                                stableau[i][j] = stableau[i + 1][j]
                                stableau[i + 1][j] = -1
                                i = i + 1
                                if stableau[i + 1][j] == 0 or i == len(stableau):
                                    if stableau[i][j + 1] == 0 or j == len(stableau.T):
                                        stableau[i][j]=0
                                        break
                            else:
                                stableau[i][j] = stableau[i][j+1]
                                stableau[i][j + 1] = -1
                                j= j+1
                                if stableau[i + 1][j] == 0 or i == len(stableau):
                                    if stableau[i][j + 1] == 0 or j == len(stableau.T):
                                        stableau[i][j]=0
                                        break
                        return stableau


def savesliding(s):                     # sliding for skewtableaux without zero rows and cols on outside
    stableau = np.concatenate((np.concatenate((s,np.zeros((len(s),2))),axis=1),np.zeros((2,len(s.T)+2))),axis=0)
    result = Sliding(stableau)
    result= np.delete(result,(-1),axis=1)
    result = np.delete(result, (-1), axis=0)
    result= np.delete(result,(-1),axis=1)
    result = np.delete(result, (-1), axis=0)
    return result

#s = np.array([[-1,  5,  7,  0,  0],[ 3,  6,  8,  0,  0],[ 6,  7,  0,  0,  0],[ 0,  0,  0,  0,  0],[ 0,  0,  0,  0,  0]])
#print(savesliding(s))