from itertools import combinations
#Amino Acids weights
weights={'R':156,
        'N':114,
        'D':115,
        'C':103,
        'E':129,
        'Q':128,
        'G':57,
        'H':137,
        'L':113,
        'M':131,
        'F':147,
        'P':97,
        'S':87,
        'T':101,
        'W':186,
        'Y':136,
        'V':99,
        'A':71}


# get the initial list of the peptide
#initial_list_of_aas
def init_list(list_of_weights):
  initial_list1=[]
  initial_list2=[]

  for i in range (len(list_of_weights)):
    weight=list_of_weights[i] 
    #get the amino acid by its key
    for aa,aa_weight in weights.items():  
      if weight==aa_weight:  
        initial_list2.append(aa)            #inital_list2 has duplication values
        if aa not in initial_list1:         #remove duplicates
          initial_list1.append(aa)          #initial_list1 has no duplications

  frequency={}   #dictionary that holds the each amino acid with its frequency

   #initialize all frequencies by zero
  for i in range (len(initial_list1)):
    frequency[initial_list1[i]]=0

  #increment all the values by its number of repetion
  for i in range (len(initial_list2)):
    frequency[initial_list2[i]]=frequency[initial_list2[i]]+1   
         
  return initial_list2,frequency


#function to return the weight of the sub_peptide
def get_weight(sub_peptide):
  sum=0
  for i in range(len(sub_peptide)):
    sum+=weights[sub_peptide[i]]
  return sum

#check the concistency of the sub_Peptide
def isConsistent(sub_peptide,thero_spect):
  weight=[]
  temp=[]  #temporary list that has a copy of the therotical spectrum
  
  #append all the values in the therotical spectrum in temp
  for i in range (len(thero_spect)):
   temp.append(thero_spect[i])

  #get all the combinations from the sub_Peptide using combinations (built in fn)
  combination=[sub_peptide[x:y] for x,y in combinations(range(len(sub_peptide)+1),r=2)]
  
  #get the weight of all combination and append them to weight[]
  for i in range(len(combination)):
    weight.append(get_weight(combination[i]))
  
  #check the consistency
  for k in range(len(sub_peptide)):
   for i in temp:
    for j in weight:
       if i==j:
        if i in temp:
          temp.remove(i)
          weight.remove(j)

  if len(weight)!=0:
     return False
  return True
                
#linear_spectrum
def linear_spectrum(initial_list,dic,therotical_spec):
  multi_mers=[]
  #drive a copy to the inital list 
  for i in range(len(initial_list)):
    multi_mers.append(initial_list[i])
  
  #Branch step
  for k in range (len(initial_list)):
   count=0
   for i in range(len(multi_mers)):
    for j in range(len(initial_list)):
      spectrum=multi_mers[i]+initial_list[j]   #extend spectrum by the initial list
      consistency=isConsistent(spectrum,therotical_spec)  #Is Consistent ? (True,False)
      flag=0
      for k in range(len(spectrum)):
        count=spectrum.count(spectrum[k]) # count the frequency of spectrum's elements
        if count> dic[spectrum[k]]: # check if the frequency allowed eg. c>2 -> not allowed
          flag=1
          break
        #Bound Step  
        if flag==0 and consistency==True:
         if spectrum not in multi_mers:
          multi_mers.append(spectrum)
  output=[]
  #get the final representations of the peptide from multi_mers
  for i in range(len(multi_mers)):
    if len(multi_mers[i])==len(initial_list):
      output.append(multi_mers[i])

  return output



if __name__ == "__main__":
    theoSpect=[]
    
    theoSpect = [int(x) for x in (
        list(input("Enter Therotical Spectrum: ").split(' '))
    )]

    unique_aa, freq = init_list(theoSpect)
    allCycloPeptides = linear_spectrum(unique_aa, freq, theoSpect)
    
    print("All Cyclo Peptides=> ", allCycloPeptides)
