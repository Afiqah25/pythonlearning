# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 22:50:18 2023

@author: AfiqahHasbullah
"""

"""
zip
Looping through 2 lists simultaneously
"""

alpha = ['a' , 'b' , 'c']
numer = [97,98,99,100]

for a,n in zip(alpha,numer) :
    print(f'ASCII code of "{a}" is {n}')
    
    
"""
Enumerate

Use enumerate to get iteration index
    - python use zero-based numbering convention
"""

msg = 'hello!'
for i, c in enumerate(msg):
    print(f'index = {i}, character = {c}')
    
    
