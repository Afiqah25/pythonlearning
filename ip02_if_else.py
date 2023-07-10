# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 18:11:53 2023

@author: AfiqahHasbullah
"""

from random import randint

dice = randint(1,6)

if dice % 2 == 0 :
    print(f'You win! Is an even number! {dice}')
else:
    print('TOO BAD,YOU LOSE')