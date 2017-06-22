# Carlos Barillas
# cbarilla@ucsc.edu
# Programming Assignment 7

"""
This module provides functions to perform standard vector operations.  Vectors
are represented as lists of numbers (floats or ints).  Functions that take two 
vector arguments may give arbitrary output if the vectors are not compatible,
i.e. of the same dimension.  
"""

import random, math

def add(u, v):
    """
    Return the vector sum u+v.
    """
    if len(u)==len(v):
        vectorSum = []
        for i in range(len(u)):
            vectorSum.append(u[i]+v[i])
    return vectorSum

def negate(u):
    """
    Returns the negative -u of the vector u.
    """
    vectorNegate = []
    for i in range(len(u)):
        vectorNegate.append(u[i]*-1)
    return vectorNegate

def sub(u, v):
    """
    Return the vector difference u-v.  
    """
    if len(u)==len(v):
        vectorDifference = []
        for i in range(len(u)):
            vectorDifference.append(u[i]-v[i])
    return vectorDifference

def scalarMult(c, u):
    """
    Return the scalar product cu of the number c by the vector u. 
    """
    vectorScalarProduct = []
    for i in range(len(u)):
        vectorScalarProduct.append(u[i]*c)
    return vectorScalarProduct

def zip(u, v):
    """
    Return the component-wise product of u with v. 
    """
    if len(u)==len(v):
        vectorProduct= []
        for i in range(len(u)):
            vectorProduct.append(u[i]*v[i])
    return vectorProduct

def dot(u, v):
    """
    Return the dot product of u with v.
    """
    myList = zip(u,v)
    dotProduct = sum(myList)
    return dotProduct

def length(u):
    """
    Return the (geometric) length of the vector u.
    """
    return math.sqrt(dot(u,u))

def unit(v):
    """
    Return a unit (geometric length 1) vector in the direction of v. 
    """
    vectorReciprocal = []
    reciprocal = 1/ length(v)
    for i in range(len(v)):
        vectorReciprocal.append(v[i]*reciprocal)
    return vectorReciprocal

def angle(u, v):
   """
   Return the angle (in degrees) between vectors u and v.
   """
   return math.degrees(math.acos(dot(unit(u),unit(v))))

def randVector(n, a, b):
    """
    Return a vector of dimension n whose components are random floats in the range [a,b).
    """
    newList = []
    for i in range (n):
        newList.append((b-a)*random.random()+a)
    return newList

