# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 21:50:05 2022

@author: Ahmed Nasser
"""


try:
    fileName = 'weight.txt'
    f = open(fileName)
    weightsDict = {}

    for line in f:
        line = line.rstrip()
        x = line.split(',')
        x[1] = int(x[1])
        weightsDict[x[1]] = x[0]

    f.close()

except IOError:
    print("File (%s) doesn't exist" % fileName)



#Extracts all the (1-mer) of the Peptide
def Initial_List(spect):
    listInit = []
    for i in range(len(spect)):
        if spect[i] in weightsDict.keys():
            listInit.append(weightsDict[spect[i]])
    return listInit



#Calculate the (k-mers) Scores
def Linear_Spectrum(peptide):
    sublist=[peptide]
    for i in range(len(peptide)):
        for j in range(len(peptide)):
            if (i+j) < len(peptide):
                 sublist.append(peptide[j:(i+j)+1])
            else:
                sublist.append(peptide[j:len(peptide)]+peptide[0:(i+j)-len(peptide)])
    return sublist



def IsConsistent(z):
    pass



def Extraction(initList):
    z = list(Initial_List(initList))

    for i in range(2, len(z)):
        z = Linear_Spectrum(z)
        IsConsistent(z)
    return z







#Main
initList = list(input("Enter Your CycloPeptide Seq: ").split(" ")).sort()

Extraction(initList)
