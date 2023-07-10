# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 18:47:43 2023

@author: AfiqahHasbullah
"""

from random import randint

for i in range(10) :
    dice = randint(1,6)
    result = 'even' if (dice % 2 == 0) else 'odd'
    print ('You draw an %s number %d.' %(result,dice))