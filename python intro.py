# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 12:11:22 2025

@author: Lenovo
"""

print ("farha")
#this is a commant
name="farha"    #string
age=20          #integer
height=1.53     # float
print (name)
print (age)
print (height)

"""taking input in python"""

name=input("enter your name:")
age=int(input("enter your age:"))
height=float(input("enter your height in meters:"))
print(f"hello,{name}your are {age} years old and {height} meters tall")

"""variabls in paython"""

a123="sample"
_name="john"
n_123=53
# 1a="sample"  # starts with a number
#n%4=100    #contains a special character
# n 9="test"  #including a space
# =============================================================================
#  """ operators in python """
# =============================================================================
# arithmatic operators
#assignmetic operators
# logical operators
# identity operators
# membership operators
## bitwise operators
""" arithamatic operators """
x=10+5    # addition 
print(x)
a=4
b=5
print(a+b)
#### subtraction###
a=6
b=3
print(a-b)
### maltiplication ###
5*6
a=8
b=4
print(a*b)
###  divition  ###
X=12/3
print(x)
a=56
b=33
print(a/b)
    ### floor divition ###
a=10
b=4
print(a//b)
### modulas ###
y=33%3
print(y)
### exponention ###
x=2**4
print(x)
### assignment operators ###
a=5
print (a)
a+=2
print(a)
a*=3
print (a)
a//=5
print(a)
  ### comparisan operators ###
a=10
b=3
print (a==b)
print (a!=b)
print (a<b)
print (a>b)
print(a<=b)
print(a>=b)
### logical operators ###
x=True
y=False
print(x and y)
print(x or y)
print (not x)
print(not y)
x=(10>5)and(5<10)
print(x)
x=(10>5) or (5>10)
print(x)
x= not 10>5
print(x)
   ### identity operators###
a=[1,2,3]
b=a
c=[1,2,3]
print (a is b)
print (a is c)
print (a is not c)
fruits= ["apple","orange","mango"]
vegetables=["cucumber","tomato","onion"]
salad=fruits
print (fruits is vegetables)
print (fruits is salad)
print(fruits is not vegetables)
    ###  membership operators  ###
numbers=[1,2,3,4,5]
print (3 in numbers)
print (5 in numbers)
print(7 in numbers)
 ### bitwise operators  ###
a=5       #0101
b=3       # 0011
print (a & b)
print (a|b)
print (a^b)      
print (a<<1)    #left shift
print (a<<2)    #right shift
a=20
binary_a=bin(20) 
print (binary_a)
print (bin(5))
print(bin(20)[2:])
    ###datatype in python ###
         #numaric  data type
# int - repressents integer , eg. 10,1,2,75,-10,100
# float- represents decimal number or point number eg. 1.6,3.14
        #sequence data type
#str - represent string (text),eg."hello""name"
#list- represents ordered collection of itemes,eg.[1,2,3,4],["appile","banana""cherry"]
#tuple- represents ordered immudable or unchengabel collection of items,eg.(1,2,3)
       # mapping datatype
#dict -represents dictionary (key valus pairs)eg.name: "alice"
       #set data type
#set-represents unordered items of unique itemes,{1,2,3}{"apple""banana""cherry"}
# frozen set -represents immutable or unchengable set,eg.frozenset([1,2,3])  
      #boolien data type
#bool-represents boolin values ,eg. true,false
      ###checking data type###
type(3)
type(2.4)
type("farha")
type(True)

"""LIST"""

#eg.numbers=[1,2,3,4,5,6]
fruits =["apple","banana","cherry"]
fruits[0]
fruits[1]
fruits[2]
fruits.append("orenge")
print (fruits)

"""LIST METHODS"""

# list is a collection of an ordered sequence of items . valuesof list are mutable(can be changed) 
#valus are arrenged in a square brakect value in a list are called elaments or items


#extend():
fruits.extend ("apple")
print (fruits)
fruits=["apple","banana","cherry"]

#insert():
fruits.insert(2,"orange")
print(fruits)

#index():returns the index of the first occurrence of a specifed value 
furits=["apple","banana","cherry"]
fruits.index("cherry")
print(fruits)
#count():returns the number of occurrences of a specified value.
fruits.count("apple")

#sort():
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print (fruits)

#pop():
fruits.pop()
print(fruits)
fruits.pop(0)
print (fruits)
fruits=["apple","banana","cherry"]
#remove():
fruits.remove("banana")
print(fruits)
#clear():
fruits.clear()
print(fruits)

""" List Functions """
#len:    
my_list=[1,2,3,4]
print(len(my_list))

numbers=[20,30,10,5]
print(max(numbers))
print(min(numbers))
numbers=[2,1,3,4]
print(sorted(numbers))

#slicing :(start,stop,step,) methods
fruits=["apple","banana","cherry","dates","mulbarry","fig"]
fruits[5]
fruits[1:4]
fruits[0:3]
fruits[3:6]
fruits[0:6:2]
fruits[0:6:3]
fruits[0:6:0]
fruits[0:]
fruits[:6]
fruits[:4]
fruits[2:]
fruits[::-1]
fruits[-4:-2]
   
"""Tuple"""

my_tuple=(1,2,3)
print(my_tuple)
print(my_tuple[0])
#tuple methods 
numbers=(1,2,3,4,)
print(numbers.count(3))
numbers=(10,20,30,40)
print (numbers.index(20))

"""SET"""

my_set={1,2,3,4}
print(my_set)
s={1,2,2,3,4,4}
print(s)
my_frozenset=frozenset([1,2,3,4])
print(my_frozenset)
my_frozenset.add(4)

"""set methods""" 
     
#add:Adds an element to the set   
s={1,2,3}
s.add(4)
print(s)

#clear:removes all elements from the set
s={1,2,3}
s.clear()
print (s)#output:set()

#copy:returns a shallow copy of the set.
s={1,2,3}
new_set=s.copy()
print(new_set)

# discart: remove the specified element from the set (if present).
s={1,2,3}
s.discard(4)#no error
print(s)#output:{1,2,3}

#pop:removes and returns anarbitrary element form the set.
s={10,20,30}
val=s.pop()
print(val)
print(s)

#remove:removes the specified element from the set. (raises keyerror if the element is not present)
s={1,2,3}
s.remove(2)
s.remove(4)
print(s)#output:[1,3]

#defferance:returns the diffrence between two or more sets.
a={1,2,3}
b={2,3,4}
print(a.differance(b))#{1}

#differance_update:removes all element of anather set from this set.
a={1,2,3,4}
b={3,4,5}
print(a.difference_update(b))
print(a)
print(b)

r={'cristiano','tony','ramos','navas'}
p={'messi','neymer','m.bappa','ramos','navas'}
r.difference_update(p)
print(r)
print(p)

#intersaction:returns the intersaction of two or more set.
a={1,2,3}
b={2,3,4}
print(a.intersection(b))#{2,3}

#union
a={1,2}
b={3,4}
print(a.union(b)) 

#update :update the set union of its self and other
s={1,2}
s.update({3,4},{5,6})
print(s)

#symmetric difference
a={1,2,3}
b={3,4,5}
print(a.symmetric_difference(b))

#isdisjint
a={1,2}
b={3,4}
print(a.isdisjoint(b)) 
c={2,3}
print(a.isdisjoint(c))

#issubset
a={1,2}
b={1,2,3}
print(a.issubset(b)) 

#issuperset
a={1,2,3}
b={2,3}
print(a.issuperset(b))

"""Dictionary"""
  
# A dictionary is an unordered collection of key_value pairs.
# each key in dictionary must be unique,and keys are used to accessthe corresponding values.
#Dictionariesare mutable,meaning you can change,add,and remove items.
#key characteristics:
#unordered:items are not in aspecific order.
#mutable:you can modify the dictionary in place.
#key-value paris:each items consistence of a key and a values.
#unique keys:keysmust be unique, but value can be duplicated
#creating dictionary


#crating an empty dictionaries
my_dict={}
print(my_dict)
#criating a dictionary with initial values:
my_dict={"name":"alice","age":25,"city":"new york"}
print(my_dict)
#accessing values by key 
print(my_dict["name"])
#adding or modifuing values:
my_dict["age"]=26
my_dict["country"]="usa"
print(my_dict) 
#removing key-value pairs:
del my_dict ["city"]   
print(my_dict)
age= my_dict.pop("age")
print(age)
print(my_dict)
print(my_dict.clear)

"""Dictionary Methods"""

# get()retuns the value for a specifid key is in the dictionary, otherwise returns a default values
student={'name':'murshi','age':21}
print(student.get('name'))
print (student.get('grade'))
print (student.get('grade','N/A'))

#key():returnce a view object that displays a list of all the keys
student={'name':'murshi','age':'21'}
print(student.key())

#values():returns a view obeject that displays a list of all the keys.
student={'name':'murshi','age':21}
print(student.values())

#items():returns a view object that displays a list of dictionary's key-value tuple pairs.
student={'name':'murshi','age':21}
print(student.items())

#updata()updates the dictionary with the element from an iteerable of key-value pairs
student={'name':'murshi','age':21}
student.update({'grade':'A','age':22})
print(student)

"""Strings"""

my_string='hello,world'
print(my_string)

#concatenation:
str1="hello"
str2="world"
result=str1+" "+str2
print(result)

#repetition:
str1="ha"
result=str1*6
print(result)

#indexing
str1="hello"
print(str1[1])  
print(str1[-1])
name="murshi"
print(name[2])

#slicing
str1="hello"
print(str1[1:4])
print(str1[:2])
print(str1[2:])

"""String methods and functions """

#count():
text="hello world"
print(text.count("l"))

text="murshidha"
print(text.count("a"))


#index():
text="hello"
print(text.index("e"))
text="murshidha"
print(text.index("a"))

#concatenation
a="data"
b="analytics"
result=a+" "+b
print(result) 
      
#maximum
s="zeebra"
print(max(s))
# minimam
print(min(s))
institution="beatcenterofexcellence"
print(max(institution))
print(min(institution))

#delete
s="hello"
new_s=s[:1]+s[2:]
print(new_s)
institution="beat"
institution=institution[:1]+institution[2:]
print(institution)

#replace
s=s.replace("l","y")
print(s)

#capitalize
text="python"
print(text.capitalize())
#lower
text="HELLO"
print(text.lower())
#upper
text="hello"
print(text.upper())

#strip
text="hello "
print(text.strip())

#swapcase
text="PyThOn"
print(text.swapcase())                  

#center
text="murshi"
print(text.center(12,'-'))

#isalnum   * alpha numeric
text="abc123"
print(text.isalnum())

#isdigit
num="123"
print(num.isdigit())

#isalpha
text="python"
print(text.isalpha())

#isspace
text=" "
print(text.isspace())

#startswith
text="data analytics"
print(text.startswith("data"))
#endswith
print(text.endswith("data"))



#--------
a="5"
b="10"
result=a+b
print(result)
#--------

""" String Formating """

name="farha"
age=20
salary=6000
formatted_str="name:{0},age:{1},salary:{2}".format(name,age,salary)
print(formatted_str)

#f-strings(formatted string literals)
name="farha"
age=30
formatted_str=f"Name:{name},Age:{age}"
print(formatted_str)
a=10
b=5
print(f"the sum of {a} and {b} is {a+b}")

""" Conditional Statements in Python """

#conditional statment in python allow you to execute different blocks of code based on whether a condithion

"""if statement"""
x=10
if x >5:
 print("x is >5")
x=13
if x <15:
  print("x is <15")
age=17
if age <18:
    print("you are not eligible to vote") 


#else
x=11
if x>9:
   print("x is greater then 9")
          
else:
    print("x is not greater than 9")
    
salary=50000
if salary >60000:
    print("He must pay the tax")
else:
    print("He not eligible to pay tax")
    
"""if else elif statement"""

# The if...elif...else statement allows you to check multiple conditions sequentially.
# it executes the first block of code whose condition is true,and skips the rest.
x=10
if x>5:
    print("x is greater than 5")
elif x==5:
    print("x is equal to 5")
else:
    print("x is less than 5")
    
#suppose a teacher wants to Assign grades based on a students score:

# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# Below 60 F

  
 
age = int(input("enter your age:"))
if age>=18:
    print("You are eligible for a driving license.")
elif age>=16:
    print("You are eligible for a learner's permit. ")
else:
    print("You are not eligible to drive yet.")
    
age =int(input("enter your age"))   
if age<=18:
    print("you are not eligible to vote")
elif age>=19:
    print  ("you are eligible to ingore ")
else:
    print("you are eligible to vote")
    
charge=int(input("enter your charge"))
if charge>=20:
    print("charge level is fine.")
elif charge<=10:
    print("charge getting low")
else:
    print("low charge plug in your charger")
    
""" Nested if satatement """
age=20
citizenship="UK"
if age>=18:
   if citizenship=="USA":
     print("you are eligible to vote.")
     print("you are the a citizen of the united states.") 
   else:  
     print("you are not a citizen of the united states.")     
else:
    print("you are not eligeble to vote because you are under 18 years old")


balance=5000
atm_pin=1234

user_pin=int(input("enter your ATM PIN."))
if user_pin==atm_pin:
    amount=int(input("enter amount to withdraw:"))
    if amount <=balance:
        if amount % 100==0:
            print(f"please collect your cash {amount}")
        else:
            print("Amount must be in multiples of 100.")
    else:
        print("insufficient balance.")
else:
     print("invalid PIN.")
     
"""LOOPS in Python """
  
# LOOP in python allows you to repeatedly executes a block of code as long as a condition is true 
#(while loop) orfor a specifide number of times (for loop).
# these are fundamental constructs for iterating over sequences,processing data,and automating repetitive tasks.

num=1 
while num <=10:
    print(num)
    num +=1
    
    
# while loop  

correct_pin="1234"
attempts=0
max_attempts=3
while attempts < max_attempts: 
    pin=input("enter your ATM pin:")
    if pin==correct_pin:
        print ("access granted")
        break
    else:
        attempts +=1
        print("incorrect pin")
        
if attempts ==max_attempts:
    print("card blocke.too many wrong attempts")
    
 # for loop
 
names=["fayiz","murshidha","farha"]
for name in names:
    print(name)

fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)
    
marks=[85,90,78,92]
totel=0
for mark in marks:
    totel += mark
print("totel marks:",totel)
    
#
marks=[78,55,89,92,67]
for mark in marks:
    if mark>=60:
        print("pass:",mark)
    else:
        print("fail",mark)
    
    
students=["fayis","murshi","farha","midhilaj"]
for student in students:
     print(f"remainder {student},please submit your assignment by to night")
     
""" loop control statement """

#break
num=1
while num<=5:
    print(num)
    if num==3:
        break
    num+=1
    
students=[("amina",89),("ravi",99),("sara",78),("john",100)]
for name,marks in students:
    if marks==100:
        print(f"{name} has full marks ! stopping the search.")
        break
    print(f"checked {name}'s mark")
    
    

     

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        




      
    

    
    
    
    

   
