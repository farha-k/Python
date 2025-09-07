# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 19:09:39 2025

@author: saofl
"""

op = input("Enter your choice (+, -, *, /): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if op == '+':
    result = add(a, b)
elif op == '-':
    result = subtract(a, b)
elif op == '*':
    result = multiply(a, b)
elif op == '/':
    result = divide(a, b)
else:
    result = "Invalid operator"

print("Result:", result)
