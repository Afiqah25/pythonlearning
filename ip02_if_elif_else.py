# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 18:16:59 2023

@author: AfiqahHasbullah
"""

from random import choice

wdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

today = choice(wdays)

if today == 'Friday' :
    print(f"Thank God, it's {today}")
elif today == 'Monday' or today == 'Tuesday':
    print(f'I eat Nasi Lemak on {today}')
elif today in ['Wednesday','Thursday']:
    print(f'{today} is tom yam day!')
else:
    print(f'Hooray!{today} is weekend!')