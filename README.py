# Bio_Computing
Bio Computing Coursework 1
"""
Created on Tue Nov 08 11:31:37 2016

@author: Wil
"""
# genetic algorithm to minimise function 4 + x + 2y = 0
import numpy as np
import random as rand
import math as ma
import bbobbenchmarks as bn

# make sure population and parent selection pans out to even numbers
# initialise 10 members of population 
popNum = 30
# percentage of population to use as parents 
parentselection = 0.6
# user set
iterations = 350

# number of parents as integers
# half of this number are children substituted back into the population
parentNum = popNum * parentselection

# instantiate function 1 on instance 0
f20 = bn.F20(0) 
# array for holding population 
population = np.zeros(shape=((4),(popNum)))
#array for holding
hold = np.zeros(shape=(popNum))
# array for multiple rankings
rank = np.zeros(shape = (popNum))
# array for holding parents 
parents = np.zeros(shape=((2),(parentNum)))
# array for holding children 
children = np.zeros(shape=((2),(parentNum/2))) 

# child counter 
childCnt = 0
# mutation probability for each population member - 5%  
mutateRate = 5
# count number of mutations
mutateCnt = 0
# amount of mutation - 10% 
mutateAmount = 0.1

# stop indicator
stop = 0

# populate array of random numbers size population, dimension 2    
def randomPop():
    for j in range(0,popNum):
        population [0][j] = rand.randint(-20,20)
        population [1][j] = rand.randint(-20,20)
        print "Pop " , j , "  X: " , population [0][j] , ", Y: " , population [1][j]
    print "\n"
    
# feed population into fitness function, store output
def feedIntoFunction():
    for j in range(0,popNum):
        x = population [0][j] 
        y = population [1][j]
            
        population [2][j] = fitFunction1(x,y)
        print "Pop " , j , "  Output : " , population [2][j]
    print "\n"    

# fitness function  
def fitFunction (x,y):
    result = 4 + 3 * x + 2*y
    return (result)

# F1 fitness function     
def fitFunction1 (x,y):
    result = f20.evaluate([x,y])
    return (result) 
    
# rank solutions and store their rank
def findRank():    
    # import all of array row into holding array
    for j in range(0,popNum):
        hold [j] = ma.fabs(population [2][j])    

    counter = 0
    rank = np.zeros(shape = (popNum))
    
    # find ith minimum  
    for i in range(0,popNum):
        
        currentMin = np.partition(hold, i)[i]

        for a in range(0,popNum):
            if currentMin == hold [a]: 
                if rank [a] != 1:   
                    print "Value " , population [2][a] , "at position" , a , "rank is " , counter

                    population [3][a] = counter
                    rank [a] = 1
                    counter += 1 
        
    print "\n" , population , "\n"
            
# store selected best solutions in parent array
def findParent():
    parentCnt = 0
    for i in range (0,int(popNum)):
        
        if population [3][i] < parentNum: 
            
            parents [0][parentCnt] = population [0][i] 
            parents [1][parentCnt] = population [1][i]

            print "Rank " , population [3][i]
            print "parents are: " , parents [0][parentCnt], parents[1][parentCnt]
            parentCnt += 1
    print parents
    print "\n"
    
# combine parents to create children 
def createChild():
    childCnt = 0
    pCnt = 0
    for j in range (0,int(parentNum)):
        if (j % 2 == 0 & j != (int(parentNum))):
            children [0][childCnt] = ((parents [0][pCnt] + parents [0][pCnt+1])/2)
            children [1][childCnt] = ((parents [1][pCnt] + parents [1][pCnt+1])/2)
            childCnt += 1
            pCnt += 2
    
    print children
    print "\n"

def randMutate(mutateCnt):
    for j in range (0, popNum):
        prob = rand.randint(-50,50)
        if prob <0:
            a = mutateAmount * population [0][j] * -1
            b = mutateAmount * population [1][j] * -1
        else:
            a = mutateAmount * population [0][j]
            b = mutateAmount * population [1][j]

        population [0][j] += a
        population [1][j] += b
        print "mutation: " , a , b
        mutateCnt += 2
    return (mutateCnt)
    
def randMutate1(mutateCnt):
    for j in range (0, popNum):
        if population [3][j] >= 1: 
            prob = rand.randint(-5,5)
            if prob <0:
                a = mutateAmount * population [0][j] * -1
                b = mutateAmount * population [1][j] * -1
            else:
                a = mutateAmount * population [0][j]
                b = mutateAmount * population [1][j]

            population [0][j] += a
            population [1][j] += b
            print "mutation: " , a , b
            mutateCnt += 2
    return (mutateCnt)
    
def randMutate2(mutateCnt):
    for j in range (0, popNum):
        if population [3][j] >= 3: 
            prob = rand.randint(0,1)
            if prob ==0:
                a = mutateAmount * population [0][j] *-1
                b = mutateAmount * population [1][j]*-1
            else:
                a = mutateAmount * population [0][j] 
                b = mutateAmount * population [1][j]
 
            population [0][j] += a
            population [1][j] += b
            print "mutation: " , a , b
            mutateCnt += 2
    return (mutateCnt)    
# randomly mutate some of the population 
def randMutateproto(mutateCnt):
    
    for j in range (0, popNum):
        prob = rand.randint(-50,50)
        if ma.fabs (prob) <= 5:
            a = mutateAmount * population [0][j]
            b = mutateAmount * population [1][j]
            print "mutation: " , a , b
            mutateCnt += 2
    return (mutateCnt)            
    
# replace worst members of the population    
def sub():
    a = 0
    for j in range (0, popNum):
        
        if population [3][j] >= (popNum - (parentNum/2)):
            population [0][j] = children [0][a]
            population [1][j] = children [1][a]
            print a
            print "New population member " , j , "  X: " , population [0][j] , ", Y: " , population [1][j]  
            a = a + 1  
    print "\n"

    
# main operating code
            
randomPop()
# count number of mutations
mutateCnt = 0

# repeat for iterations
for b in range(0,iterations):  
  
    if stop == 0: 
        feedIntoFunction()   
        # check if error acceptably small 
        for i in range(0,popNum):
            if (ma.fabs(population [2][i])) <= 1:
                stop = 1
                print "Solution is" , population [0][i] , "and" , population [1][i], "\n"
                print "Found in " , b , "iterations. \n"                     
                print "Amount of mutations" , mutateCnt, "\n"
                
    if stop == 0:
        findRank()
        #findParent()
        #createChild()
        mutateCnt = randMutate2(mutateCnt)
        #sub()     
    
    if b == iterations-1: 
        if stop == 0:
            print "No solutions found in " , b+1 , "iterations. "    
            print "Amount of mutations" , mutateCnt, "\n"        
