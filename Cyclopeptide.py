'''Team Members=>
        - Ahmed Nasser
        - Yossef Essam
        - Maryam Abdulhady
        - Amany Gamal
        - Abdulrahman Yossry
'''


from itertools import combinations
import sys


# Creates the Initial_List of 1-mers to extend the subPeptide
def Initial_List(spectWeights):
    initList1 = []
    initList2 = []
    freq = {}  # Holds each AA and its frequency

    for i in range(len(spectWeights)):
        for aa, aaWeight in weightsDict.items():  # Gets the AA by its key
            if aaWeight == spectWeights[i]:
                initList2.append(aa)  # initList2 has the duplicates
                if aa not in initList1:  # Removes duplicates
                    initList1.append(aa)

    for i in range(len(initList1)):  # Initialize all frequencies by zero
        freq[initList1[i]] = 0

    for i in range(len(initList2)):  # Increment no. of Frequency
        freq[initList2[i]] += 1

    return initList2, freq


# Checks whether a subPeptide IsConsistent with the theoSpect.
def IsConsistent(subPeptide, theoSpect):
    weight = []
    holder = theoSpect.copy()

    # Get all combinations from subPeptide
    peptideCombs = [subPeptide[x:y]
                    for x, y in combinations(range(len(subPeptide)+1), r=2)]

    # Get weights of all peptideCombs and append them to weight[]
    for i in range(len(peptideCombs)):
        weight.append(getWeight(peptideCombs[i]))

    finalWeight = validate(subPeptide, weight, holder)

    if len(finalWeight) != 0: return False
    return True


def getWeight(subPeptide):  # Gets Total of weights of a subPeptide
    sum = 0
    for i in range(len(subPeptide)):
        sum += weightsDict[subPeptide[i]]
    return sum


def validate(subPeptide, weight, holder):
    for k in range(len(subPeptide)):
        for i in holder:
            for j in weight:
                if i == j and i in holder:
                    holder.remove(i)
                    weight.remove(j)
    return weight


# Calculates the Linear_Spectrum of a protein sequence (without circulation).
def Linear_Spectrum(initList, freq, theoSpect):
    cycloPeptide = []
    multiMers = initList.copy()

    for k in range(len(initList)):  # Branch step
        spectCount = 0
        for i in range(len(multiMers)):
            for j in range(len(initList)):
                flag = 0
                spect = multiMers[i] + initList[j]  # Merge multiMers with initial_list into spect

                for l in range(len(spect)):
                    spectCount = spect.count(spect[l])
                    if spectCount > freq[spect[l]]:     # Checks if the frequency allowed
                        flag = 1
                        break

                if flag == 0 and IsConsistent(spect, theoSpect):    # Bound step
                    if spect not in multiMers:
                        multiMers.append(spect)

    # Get final representations of the cycloPeptide from multiMers
    for i in range(len(multiMers)):
        if len(multiMers[i]) == len(initList):
            cycloPeptide.append(multiMers[i])
    return cycloPeptide




'''Therotical Spectrum=>
        0 97 97 99 101 103 196 198 200 202 295 297 299 299 301 394 396 398 400 400 497
'''

if __name__ == "__main__":
    weightsDict = {}

    try:
        fileName = 'weight.txt'
        f = open(fileName)
        for line in f:
            x = line.split(' ')
            line.rstrip()
            weightsDict[x[0]] = int(x[1])
        f.close()
    except IOError:
        print("File (%s) doesn't exist" % fileName)
        sys.exit(0)

    theoriticalSpectrum = [int(x) for x in (
        list(input("\nEnter Therotical Spectrum: ").split(' '))
    )]

    unique_aa, frequencies = Initial_List(theoriticalSpectrum)
    allCycloPeptides = Linear_Spectrum(unique_aa, frequencies, theoriticalSpectrum)

    print("\tAll Cyclo Peptides=> ", allCycloPeptides)
