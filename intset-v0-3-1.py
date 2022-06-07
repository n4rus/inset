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

# In[3]:


#desired integers tested leave as zero
n=0
#amount of desired integers in the ticket
un=6


# In[4]:


#loop to random select numbers from intlist and append them to intset
def setmaker():
    #number of integers in the following set
    nlist=60
    
    #integers counter for the following set
    nl=1

    #set of integers
    mainlist=[]

    #set construction
    while nl < nlist:
        if nl <= nlist:
            i=int(nl)
            mainlist.append(i)
            nl=nl+1
        if nl > nlist:
            break
            return mainlist
            print(mainlist)    
    #loop counter
    n=0
    un=6
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


# In[5]:


#print set to verify the function
print(setmaker())


# In[6]:


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
            nlist=setmaker()
            setofsets.append(nlist)
            ni=ni+1
            ntest=ntest+1
        if ntest == testn:
            return setofsets
            break


# In[37]:


#number of tests to be done
#tests = 10000
print("Type the number of tests to run at each round:")
Tests = input()
tests = int(Tests)

#set the testsets to other variable to be handled
tst = testsets(tests)
#print(tst)


# In[38]:


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


# In[39]:


#change avg fucntion to variable for handling
#avgc = avg()


# In[40]:


#sorted_d = dict( sorted(avgc.items(), key=operator.itemgetter(1),reverse=True))
#print('Dictionary in descending order by value : ',sorted_d)


# In[45]:


#sort results to in descent order
def testtests(tn):
    #number of set of tests to run
    print("Type the number of chunks to run:")
    avgn=input()
    avgn=int(avgn)
    ni=0
    #set of sets of range  = tests
    setfsets=[]
    #loop to compose a set made of tests * avgn
    print("Total number of sets: " + str(tn*avgn))
    print("Starting task...")
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
        print('Dictionary in descending order by value : ',sorted_d)


# In[46]:


testtests(tests)


# In[ ]:





# In[ ]:




