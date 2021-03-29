import cv2 as cv
#import tkinter 
from matplotlib import pyplot as plt
import os.path
from os import path

# simple function for split hist in n part 
# view doc for example how the function split the array 
def splitHist(nPart, hist):
    totalP = sum(hist)[0]
    #print((hist[0]))
    #print('totalP:')
    #print(totalP)
    newArray =  [] 
    lPartInt, lPartDec = divmod((len(hist)/nPart),1)
    lPartInt = (int(lPartInt))
    lPartDec = (int(lPartDec * nPart))
    i=0
    # i want to make a PARTITOIN but i want to take de decimal value of division in a central part for don't influence the extreme part 
    if (nPart%2 == 0):
        extraPartIndex = int(nPart/2) - 1
    else:
        extraPartIndex = int(nPart/2)
    while(i<256):
        if(i == extraPartIndex* lPartInt):
            newArray.append(((sum(hist[i : i+lPartInt+lPartDec])[0]) / totalP))
            i += lPartInt
            i += lPartDec
        newArray.append(((sum(hist[i : i+lPartInt])[0]) / totalP))
        i += lPartInt
    print('newArray: ', newArray)
    # the sum must be ~ 1
    print('sum (must be ~1 ) :', sum(newArray))
    return(newArray)        

def decideExposition(fileDir):
    if (path.isfile(fileDir)):
        img = cv.imread(fileDir,0)
        hist = cv.calcHist([img], [0], None, [256], [0,256])
        ##view plot rappresentation 
        #plt.hist(img.ravel(),256,[0,256]);
        #plt.show()
        split = (splitHist(10, hist))
        restDx = 0
        restSx = 0
        for i,s in enumerate(split):
            if i != 0 and i != 1:
                restDx += s
            if i != len(split)-1 and i != len(split)-2:
                restSx += s
        if split[0] + split[1] > restDx and split[len(split)-1] == 0.0:
            return('under exposed')
        elif (split[len(split)-1] + (split[len(split)-2] > restSx) and (split[0]) == 0.0):
            return('over exposed')
        else:
            return('normal exposed image')
    else : 
        return('path is not a file')
    
fileDir = './imageTest/errorCase.jpg'
print(decideExposition(fileDir))
