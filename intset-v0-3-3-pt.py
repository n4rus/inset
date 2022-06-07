#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/bin/env python


# In[2]:


import random
import operator
from random import choice
from collections import Counter
from itertools import chain


# # Lotery Intset
# ### This code is intended to simulate numbers in lotery tickets and their pronability of winning

# In[4]:


print("Digite o intervalo de numeros presentes no bilhete(Ex. Inicial: 1, Final: 60 [1-60])")

#initial integer on the set)
print("Numero inicial:")
nln=input()
nli=int(nln)

#number of integers in the following set (end)
print("Numero final:")
inlist=input()
nlist=int(inlist)

#range:
print("Intervalo de numeros no bilhete: [", nln, "-", inlist, "] \n")


#loop counter
#print("Set the amount of integers to be drawn on each round:")
#amount of integers in each bet:
print("Digite o intervalo de numeros em cada aposta:")
#n=0
print("Numero inicial:")
ni=input()
n=int(ni)

#un=6
print("Numero final:")
uni=input()
un=int(uni)

#betrange
print("Intervalo de numeros no bilhete: [", ni, "-", uni, "] \n")
#number of tests to be done
#tests = 10000
print("Digite a quantidade de apostas por rodada de teste:")
Tests = input()
tests = int(Tests)


# In[5]:


#loop to random select numbers from intlist and append them to intset
def setmaker(nli, inlist, un, n):
    #number of integers in the following set
    nlist=int(inlist)
    
    #integers counter for the following set
    nl=int(nli)

    #set of integers
    mainlist=[]

    #set construction
    while nl <= nlist:
        if nl <= nlist:
            i=int(nl)
            mainlist.append(i)
            nl=nl+1
        if nl > nlist:
            break
            return mainlist
            print(mainlist)    
    #loop counter
    #n=0
    #un=6
    #create a new list to manipulate on the while
    intlist=mainlist
    intset=[]
    #loop to choose numbers and remove then from the next draw
    while n <= un:
        if n <= un:
            choice = random.choice(intlist)
            intset.append(choice)
            intlist.remove(choice)
            n=n+1
        if n > un:
            return mainlist
            print(intset)
            break


# In[6]:


#print set to verify the function
print("Alcance do intervalo:", setmaker(nli, inlist, un, n), end='\n')


# In[7]:


#define a function to make a sequence of sets and append them to a dictionary
def testsets(tn):
    #set the number of tests to run
    testn=tn
    
    #set the algorithm to take averages
    ntest=0

    setofsets=[]
    ni = 0
    while ntest <testn:
        if ntest < testn:
            nlist=setmaker(nli, inlist, un, n)
            setofsets.append(nlist)
            ni=ni+1
            ntest=ntest+1
        if ntest == testn:
            return setofsets
            break


# In[8]:


#set the testsets to other variable to be handled
tst = testsets(tests)
#print(tst)


# In[9]:


#define a function to take a probability average from the tests obtained with testsets 
def avg(tst):
    n=0
    avgcd= {}
    while n <= 60:
        for i in tst:
            for a in i:
                counts = {a:i.count(i) for a in i}
                n=n+1
    count = Counter(chain.from_iterable(tst))
#    print("Count occurrence keys:",count)        
    return count


# In[11]:


#sort results to in descent order
def testtests(tn):
    #number of set of tests to run
    print("Digite o numero de rodadas de testes:")
    avgn=input()
    avgn=int(avgn)
    ni=0
    #set of sets of range  = tests
    setfsets=[]
    #loop to compose a set made of tests * avgn
    print("Numero total de apostas: " + str(tn*avgn))
    print("Inicializando calculos...")
    while ni < avgn:
        setfsets.append(testsets(tests))
        ni=ni+1
    if ni == avgn:
        na=[]
        #creates a set composed of all numbers on the larger set
        for i in setfsets:
            for a in i:
                na.append(a)
        avgc=avg(na)
        sorted_d = dict( sorted(avgc.items(), key=operator.itemgetter(1),reverse=True))
        print('Media de Numeros sorteados ordernados de modo decrescente : ',sorted_d)


# In[12]:


testtests(tests)


# In[ ]:





# In[ ]:




