# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 21:50:05 2022
Updated on Tue Apr  5 04:59:05 2022

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


# Extracts all the (1-mer) of the Peptide
def Initial_List(spect):
    listInit = []
    for i in range(len(spect)):  # 21
        if spect[i] in weightsDict.keys():
            listInit.append(weightsDict[spect[i]])

    print("listInit: %s\n" % listInit)
    return listInit


# Calculate the (k-mers) Scores
def Linear_Spectrum(peptide):
    for i in range(len(peptide)):
        for j in range(i, len(peptide)):
            subList.append(peptide[i:j+1])

    print(subList)
    return subList


def IsConsistent(fragSpect):
    total = 0
    weightsList = []
    wl = []

    for i in range(len(fragSpect)):
        for j in weightsDict:
            if fragSpect[i] == weightsDict[j]:
                weightsList.append(j)
                wl.append(j)

    wlLength = len(weightsList)

    for i in range(wlLength):
        total += weightsList[i]
        for j in range(i, wlLength):
            tmp = weightsList[i] + weightsList[j]
            wl.append(tmp)

    wl.append(total)

    print(wl)
    return


def Extraction(initList):
    y = Linear_Spectrum(Initial_List(initList))

    for i in range(len(y)):
        IsConsistent(y[i])
    return





if __name__ == "__main__":
    '''TestCase -> Theoritcal Spectrum:
                0 97 97 99 101 103 196 198 200 202 295 297 299 299 301 394 396 398 400 400 497
    '''

    subList = []
    initListSpect = [int(x) for x in (
        list(input("Enter Your CycloPeptide Seq: ").split(' '))
    )]
    initListSpect.sort()

    Extraction(initListSpect)
