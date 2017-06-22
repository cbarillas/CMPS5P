# Carlos Barillas
# cbarilla@ucsc.edu
# Program Assignment 4
# This program checks a positive integer n from user input then prints out the first n prime numbers.

import math

def isPrime(m, L):
    for number in L:
        if m % number == 0:            # Checks if m is composite.
            return False
    return True                        # If m is not divisible by any number in L, m is prime.

numberOfPrimes = int(input("Enter the number of Primes to compute: "))
print()
primeList = [2]                        # primeList holds at least one prime number.
sqrtN = int(math.sqrt(numberOfPrimes))

for number in range(3, sqrtN+1):       # Initializes primeList to store several prime 2 <= p <= sqrt(n).
    primeFound = True                  # True if number is prime.
    for i in range(2, number):
        if (number % i == 0):          # Divides number by i from 2 to number to see if number is composite.
            primeFound = False
    if primeFound:
        primeList.append(number)       # Append number to primeList if True(i.e. number is prime).

print("The first {} primes are: ".format(numberOfPrimes))
pListLength = len(primeList)           # Length of primeList.
testPrime = 3
while pListLength < numberOfPrimes:
    if isPrime(testPrime, primeList):  # If testprime number is prime append to primeList.
        primeList.append(testPrime)
        pListLength += 1               # Increase length of list.
    testPrime += 2                     # Increases test prime by 2.

for i, prime in enumerate(primeList):  # Enumerates our list so we can use an index and items in primeList.
    print(prime, '', end ='')          # Prints out each prime separated by space, end appends a space instead of new line.

    if (i+1) % 10 == 0:                # If index of primeList is divisible by 10 then print new line.
        print()

print()
