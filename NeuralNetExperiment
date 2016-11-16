# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:41:24 2016

@author: Wil
"""

import numpy as np
import math as ma
import random as rand
import bbobbenchmarks as bn
    

# topology 

# define initial parameters
# 1 input -> 3 input nodes -> output
# alter to change network
numLayers = 3

inputAmount = 8
# define inputs using array
#ia = np.array([ [1],[2],[3],[4],[5],[6],[7],[8] ]) 
ia = np.zeros(shape=(inputAmount))

# instantiate function 1 on instance 0
f1 = bn.F1(0)

# define target outputs using array
#ta = np.array([ [1],[4],[6],[16],[25],[36],[49],[64] ])
ta = np.zeros(shape=(inputAmount))
    
# array to store number of neurons initialised to 
numNeurons = np.zeros(shape=(numLayers), dtype = int)

# array to store the number of weights in each layer 
layerWeight = np.zeros(shape=(numLayers), dtype = int)

#alter to change network
numNeurons [0] = 1
numNeurons [1] = 3
numNeurons [2] = 1

maxNeurons = 0
maxWeights = 0

# define array of errors
ea = np.zeros(shape=(inputAmount))

# define array of outputs
oa = np.zeros(shape=(inputAmount)) 




##### GA Paramters and Functions #######
# make sure population and parent selection pans out to even numbers
# initialise 10 members of population 
popNum = 3 * inputAmount
# percentage of population to use as parents 
parentselection = 0.5
# user set
iterations = 500

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
mutateAmount = 0.5

# stop indicator
stop = 0


#########################################

########### GA Functions ###############

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
        if population [3][j] >= 6: 
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
    
####################################


def calculateInitial():
# fill input array with set of random numbers  
    for i in range (0,inputAmount):
        ia [i] = rand.randint(-20,20)
    print "Random Inputs are: " , ia 

    # fill target arraay with corresponding   
    for i in range (0,inputAmount):
        ta [i] = f1.evaluate([ia [i]])
    print "Targets are: " , ta
 
def randomWeight():
# populate weight with random number between -3 and 3
    for j in range(1,(numLayers)):
        print "\nLayer ", j
    
        # for each neuron
        for k in range(0,numNeurons[j]):    
            print "Neuron " , k 
        
            # print the weights going into each of the neurons
            for l in range(0,numNeurons[j-1]):
                
                wa [j][k][l] = rand.randint(-3,3)                
                print"   value ", wa [j][k][l] 
    
def randomWeight1():
# populate weight with random number between -3 and 3
    d = 0
    for j in range(1,(numLayers)):
        print "\nLayer ", j
    
        # for each neuron
        for k in range(0,numNeurons[j]):    
            print "Neuron " , k 
        
            # print the weights going into each of the neurons
            for l in range(0,numNeurons[j-1]):
               
                if j == 1:
                    wa [j][k][l] = population [0][d]                
                    d += 1
                if j == 2:
                    wa [j][k][l] = population [1][d]
                    d+=1
                print"   value ", wa [j][k][l] 



def NeuralNetwork(b):
# print neurons and weight
# for each layer
    d = 0
    e = 0
    # pass input through to each neuron 
    for i in range(0,inputAmount):
        print "\n\nInput ", (i+1) , "is ", ia [i]
       
        if b == 0:
            randomWeight()
        else:
            randomWeight1()
        
        for j in range (1,(numLayers)):
           # sa [j-1][l] = ia [i]
            for k in range(0,numNeurons[j]):
               sa[j][k] = 0
        
        sa [0][i] = ia [i]    

        for j in range(1,(numLayers)):
            print "\nLayer ", j
    
            # for each neuron
            for k in range(0,numNeurons[j]):    
                print "Neuron " , k 
        
                # print the weights going into each of the neurons
                for l in range(0,numNeurons[j-1]): 

                    print "weight is ", wa [j][k][l]

                    # sum [layer], [neuron in previous layer]
                    sa [j][k] = sa [j][k] + (sa [j-1][i] * wa [j][k][l])
                    
                    if j == 1:
                        population [j-1][d] = wa [j][k][l]
                        d+=1
                    if j == 2:
                        population [j-1][e] = wa [j][k][l]
                        e+=1
                        
                print sa[j][k]
                   

        ea [i] = ta [i] - sa[j][k]
        population [2][e-3] = ea [i]
        population [2][e-2] = ea [i]             
        population [2][e-1] = ea [i]
        print "error is" , ea [i]

    print "\n" 
    #print ma.tanh(-5)
 

             
######## main operating code ###########
            
# count number of mutations
mutateCnt = 0

# find maximum parameters needed for matrix creation  
for i in range(1,numLayers):
    layerWeight [i] = numNeurons [i] * numNeurons [i-1]
    
    if i != (numLayers-1):
        print "Total weights for layer ", i, "are: ", layerWeight[i]
    else:    
        print "Total weights for Output are:   ", layerWeight[i]
    
    # find max amount of neurons
    if numNeurons [i] > maxNeurons:
        maxNeurons = maxWeights = numNeurons [i]

# define array for storing sum     
sa = np.zeros(shape=((numLayers),(maxNeurons*10)))

# define weights using array
wa = np.zeros(shape=((numLayers),(maxNeurons),(maxWeights)))
# repeat for iterations

calculateInitial()
randomWeight()

for b in range(0,iterations):  
    
    
    if stop == 0:
        NeuralNetwork(b)
        print population   
        # check if error acceptably small 
        for i in range(0,popNum):
            if (ma.fabs(population [2][i])) <= 1:
                stop = 1
                print "Solution is" , population [0][i] , "and" , population [1][i], "\n"
                print "Found in " , b , "iterations. \n"                     
                print "Amount of mutations" , mutateCnt, "\n"
                
    if stop == 0:
        findRank()
        findParent()
        createChild()
        sub()
        mutateCnt = randMutate2(mutateCnt)
             
    
    if b == iterations-1: 
        if stop == 0:
            print "No solutions found in " , b+1 , "iterations. "    
            print "Amount of mutations" , mutateCnt, "\n"
