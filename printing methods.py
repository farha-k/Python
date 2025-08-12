# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 14:57:15 2025

@author: saofl
"""

""" String Formatting"""

### Formatting with placeholders ###

print("I'm going to inject %f here."%12)
print("hai %5.3f"%3)
a="pradeep"
b="hari"
print("hello my name is %r \n %r"%(a,b))
print("I'm going to inject %s text here,and %s text here."%('some','more'))
a=12
a
a
print(13)
x,y='some','more'
print("I'm going to inject %s text here,and %s text here."%(x,y))

### format conversion methods.

print("He said his name was %s."%'fred')
print("He said his name was %r."%'Fred')
print("%r"%12)
print("I once caught a fish %s."%'this \tbig')
print("I once caught a fish %r."%'this \tbig')
print("I wrote %s programs today."%3.75)
print("I wrote %d programs today."%3.75)

### padding and precision of floating point numbers.

print("floating point numbers:%5.2f"%(13.144))
print("floating point numbers:%1.0f"%(13.144))
print("floating point numbers:%1.5f"%(13.144))
print("floating point numbers:%10.2f"%(13.144))
print("floating popint numbers:%25.2f"%(13.144))

### multiple formatting.

print("First:%s,Second:%5.3f,Third:%s"%("hi",3.1415,"bye"))

### Formatting with the .format() method ###

print("This is a string with an {}".format('insert'))

### The format() method has several advantages over the %s placeholder method:
    
#1.insert objects can be called by index position:
print("The {2} {1} {0}".format('fox','brown','quick'))    
#2.inserted objects can be assigned keywords:
print('First Object:{a} Second Object:{b} Third Object:{c}'.format(a=1,b='two',c=12.3))    
a=34
b='hai'
c=True
print('First Object:{a} Second Object:{b} Third Object:{a}'.format(a=34,b='ai',c=34.5))

#3.inserted objects can be reused,avoiding duplication:
print("A %s saved is a %s earned."%("penny","penny"))    
#vs
print("A {p} saved is a {p} earned.".format(p='penny') )

### Allignment,padding and precision with .format()

print("{0:<8} | {1:^8} | {2:>8}".format('Left','Center','Right'))
print("{0:<8} | {1:^8} | {2:>8}".format(11,22,33))
print("{0:=<8} | {1:-^8} | {2:.>8}".format('Left','Center','Right'))
print("{0:=<8} | {1:-^8} | {2:.>8}".format(11,22,33))
print("This is my ten-character,two-decimal number:%10.2f"%13.579)
print("This is my ten-character two-decimal number:{1:s}".format(13.579,'12'))

### Formatted string literals(f-strings)  ###

num=23.45678
print("My 10 character,four decimal number is:{0:10.4f}".format(num))
print(f"My 10 chracter ,four decimal number is :{num:{10}.{6}}")

num=23.45
print("My 10 character,four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character four decimal number is:{num:10.6f}")
