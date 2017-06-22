# Carlos Barillas
# cbarilla@ucsc.edu
# Program Assignment 5

import sys

print('Enter two numbers, low then high.')
n = int(input('low = '))
m = int(input('high = '))
print()

while n>m:
    print('Please enter the smaller followed by the larger number.')
    n = int(input('low = '))
    m = int(input('high = '))
    print()
    if n<m:
        break

myList = []  # Create an empty list to store numbers from n to m.
for number in range(n, m+1):
    myList.append(number)  # Appends the numbers from n to m to myList.

print('Think of a number in the range {} to {} range. \n'.format(n, m))

numberOfGuesses = 0
if n == m:  # When our bounds are the same.
   print('Your number is {}. I found it in {} guesses.'.format(n, numberOfGuesses))
   sys.exit()

left = 0  # The index for the first element of myList.
right = len(myList) - 1  # The index for the last element of myList.

while left <= right:  # Exactly like binary search from example given.
    midpoint = (left+right)//2
    print('Is your number Less than, Greater than, or Equal to {} ?'.format(myList[midpoint]))
    p = input("Please type 'L', 'G' or 'E': ")
    print()

    if p == 'L' or p == 'l':  # If our number is less than myList[midpoint]
        numberOfGuesses += 1  # Increment guess number, aka our counter.
        right = midpoint - 1  # Our right index becomes midpoint - 1.
        if left == right:  # If the indices match then we're only looking at one number in our list, which is our number. 
            print('Your number is {}. I found it in {} guesses.'.format(myList[right], numberOfGuesses))
            break
        if left > right:  # If left index is greater than right index something isn't right, the answers don't make sense. 
            print('Your answers have not been consistent.')
            break

    elif p == 'G' or p == 'g':  # If our number is greater than myList[midpoint]
        numberOfGuesses += 1
        left = midpoint + 1 # Our left index becomes midpoint + 1.
        if left == right:
            print('Your number is {}. I found it in {} guesses.'.format(myList[right], numberOfGuesses))
            break
        if left > right:
            print('Your answers have not been consistent.')
            break

    elif p == 'E' or p == 'e':  # If our number is equal to myList[midpoint]
        numberOfGuesses += 1
        print('I found your number in {} guess.'.format(numberOfGuesses))  # Print number of guesses it took.
        break

    else:
        p = input("Please type 'L', 'G' or 'E': ")

                                                                      

