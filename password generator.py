# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 13:59:32 2025

@author: saofl
"""

import random
import string
length=int(input("enter password length:"))
use_letters=input("include letters?(y/n):").lower()=="y"
use_digits=input("include digits?(y/n):").lower()=="y"
use_symbols=input("include symbols?(y/n):").lower()=="y"
characters=""
if use_letters:
    characters +=string.ascii_letters
if use_digits:
    characters+=string.digits
if use_symbols:
    allowed_symbols="!@#$%^&*_-"
    characters+=allowed_symbols
if not characters:
    print("you must choose at least one character set!")
else:    
    password=''.join(random.choice(characters)for _ in range(length))
print("your  generated password is:",password)