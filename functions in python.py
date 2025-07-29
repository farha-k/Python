# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 18:42:25 2025

@author: saofl
"""

""" Functions in python """

def demo():
    pass    

demo()

def demo1():
    print("hai")
    
demo1()

def demo2(name):
    print("hai",name)    
    
demo2()
demo2("pradeep")
help=demo2("pradeep")
help 

def demo3(name):
    return "hai "+name   
    
demo3("pradeep")
help1=demo3("pradeep")
help1

def demo4():
    value=1
    while value<101:
        if 49<value<61:
            value+=1
            continue
        print(value)
        value+=1

demo4()

def palindrome():
    string=input("enter a string:")
    j=-1
    for i in range(0,len(string)):
        if string[i]!=string[j]:
            print("the string is not palindrome")
            break
        j+=-1
        if i==len(string)-1:
            print("the string is a palindrome")
            
palindrome()            

def prime():
    number=int(input("enter a number:"))
    if number <=1:
       print("not a prime number")
    else:
        is_prime=True
        for i in range(2,number):
            if number%i==0:
                is_prime=False
        if is_prime:
            print("the number is prime")
        else:
            print("the number is not prime")
 
prime()            

def prime(number):
    if number <=1:
       print("not a prime number")
    else:
        is_prime=True
        for i in range(2,number):
            if number%i==0:
                is_prime=False
        if is_prime:
            return True
        else:
            return False
prime(3)        

list11=[10,15,20,25,30]
def sum_of_list(list_name):
    total=0
    for i in list_name:
        total+=i
    return total

sum_of_list(list11) 


def pattern(value,num):
    for i in range(1,num):
        print(value*i)
        
pattern("*",10)        


def pattern(value="*",num=6):
    for i in range(1,num):
        print(value*i) 
pattern(num=10,value="$")

def sep_of_even_and_odd(start,end):
    even=[]
    odd=[]
    for number in range(start,end+1):
        if number%2==0:
            even.append(number)
        else:
            odd.append(number)
    return even,odd    

even,odd=sep_of_even_and_odd(1, 100)    
even   
odd

def sep_of_words(list_name):
    char_3_words=[]
    char_morethan3_words=[]
    for i in list_name:
        if len(i)==3:
            char_3_words.append(i)
        else:
            char_morethan3_words.append(i)
    return char_3_words,char_morethan3_words        

list12=["red","blue","hai","black","white","his"]
sep_of_words(list12)
dir(str)

def sep_of_letters(sentance):
    uppercase_letters=[]
    lowercase_letters=[]
    numbers=[]
    others=[]
    for i in range(0,len(sentance)):
        j=sentance[i]
        if sentance[i].isupper():
            uppercase_letters.append(j)
        elif sentance[i].islower():
            lowercase_letters.append(j)
        elif sentance[i].isnumeric():
            numbers.append(j)
        else:
            others.append(j)
    return uppercase_letters,lowercase_letters,numbers,others                
sep_of_letters("My name is Fathima Faraha.K,my age:20")       


def summ(a,b):
    return a+b
summ(1,5,6)
def summ1(list1):
    result=0
    for value in list1:
        result+=value
    return result

summ1([1,2,3,4,5,6])



def summ1(*args):
    print(args)
    result=0
    for value in args:
        result+=value
    return result
summ1(1,6,8)

def upper(*word):
    for value in word:
        if value.isupper():
            print(value)
upper("Kerala","hai","FARAHA","GREEN")          
dir(dict)
dictionary={'name':'farha','age':20,'place':'kizhisseri','course':'data analytics','grade':'A'}
for key,values in dictionary.items():
    print(key,":",values)
    
def dictionary(**value):
    for key,values in value.items():
        print(key,":",values)
dictionary(name='farha',age=20,course='mathematics',mark_in_maths=80,mark_in_statistics=89)  
