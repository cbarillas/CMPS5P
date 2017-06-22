# Carlos Barillas
# cbarilla@ucsc.edu
# Programming Assignment 6
# Simulates throwing a pair of dice many times. Prints the sum and calculates the
# frequency of each roll, relative frequency and experimental probability. 
#--------------------------------------------------------------------------------

import random

rng = random.Random() # Create a random number generator
rng.seed(237)

def throwDice(m,k):
    """
    throws m independent dice and returns the result in a m-tuple
    """
    myList = []
    for i in range(m):
        die = rng.randrange(1, k+1)
        myList.append(die)
    myTuple = tuple(myList)
    return (myTuple)

#-- main ----------------------------------------------------------------------   
#Ask for user input and validate it
print()
numberofDice = int(input("Enter the number of dice: "))
#print()
while numberofDice<1:
    print('The number of dice must be at least 1')
    numberofDice = int(input("Please enter the number of dice: "))
    if numberofDice>1:
       print()

numberofSides = int(input("Enter the number of sides on each die: "))
#print()
while numberofSides<2:
    print('The number of sides on each die must be at least 2')
    numberofSides = int(input("Please enter the number of sides on each die: "))
    if numberofSides>2:
        print()

numberofTrials = int(input("Enter the number of trials to perform: "))
print()
while numberofTrials<1:
    print('The number of trials must be at least 1')
    numberofTrials = int(input("Please enter the number of trials to perform: "))
    if numberofTrials>=1:
        print()

# Calculates the range of possible sums and adds them to a list.
sumList = []      #Create a list to contain the range of sums     
sideDiceProduct = numberofDice*numberofSides
for i in range(sideDiceProduct+1):
    sumList.append(i)

# Finds the frequency of each roll and adds it to a list.
frequency = len(sumList)*[0]  # Our list has to have the same number of elements as sumList
for i in range(numberofTrials):
    t = throwDice(numberofDice, numberofSides)
    frequency[sum(t)] += 1

# Calculates relative frequencies.
relativeFrequency = []
for i in range(len(frequency)):
   relativeFrequency.append(frequency[i]/numberofTrials)

# Calculates expiremental probabilities.
expProbability = []
for i in range(len(relativeFrequency)):
   expProbability.append(relativeFrequency[i]*100)

# print results in a table 
f1 = "{0:<8}{1:<14}{2:<23}{3:<24}"
f2 = 70*"-"
f3 = "{0:>3}   {1:>8}{2:>18.5f}                 {3:>10.2f} %"
print(f1.format("Sum","Frequency","Relative Frequency", "Experimental Probability"))
print(f2)
for i in range(numberofDice, len(frequency)):
   print(f3.format(sumList[i], frequency [i], relativeFrequency[i], expProbability[i]))
#end for
print()
