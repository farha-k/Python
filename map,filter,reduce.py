# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 15:01:30 2025

@author: saofl
"""

list1=[1,2,3,4,5]
list2=[]
for i in list1:
    j=i**2
    list2.append(j)
print(list2)    

def square(a):
    return a**2

list(map(square,list1))

list(map(lambda a:a**2,list1))

list2=[10,20,30,40,50]
total=0
for i in list2:
    total+=i
print("the sum is",total)

from functools import reduce

def summ(a,b):
    return a+b

reduce(summ,list2)
reduce(lambda a,b:a+b,list2)

maximum=list2[0]
for i in list2:
    if i>maximum:
        maximum=i
print("the maximum value is",maximum)        

def maximum(list_name):
    maximum=list_name[0]
    for i in list_name:
        if i>maximum:
            maximum=i
    return maximum  
    

def maxx(a,b):
    if a>b:
        return a
    else:
        return b
    
reduce(maxx,list2)    
reduce(lambda a,b:a if a>b else b, list2)
reduce(lambda a,b:a if a<b else b,list2)

list3=[10,15,20,25,30,35,40,45,50,55]
divisible_by_3=[]
for i in list3:
    if i%3==0:
        divisible_by_3.append(i)
print(divisible_by_3)        
def divi3(a):
    if a%3==0:
        return False
    else:
        return True
    
list(filter(divi3,list3))
list(filter(lambda a:True if a%3==0 else False,list3))
