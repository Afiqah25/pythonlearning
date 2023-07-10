# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 21:55:10 2023

@author: AfiqahHasbullah
"""

 """
 Mutable containers :
list - for handling items one after another one
dict - for accessing items without specific order
set - for unique item set

Immutable containers :
tuple - for declaring a set of parameters
str - string data types


"""
#List


data = [1,2,3,4.0,'five'] #element can be mixed

data[0] #indexing, answer = 1 , value at location 0

data[0:2] #slicing, answer = [1,2] , value start at location 0 until 2 steps from it

data[-1] #negative index, answer = 'five', value starts from the back of handphone

data[0] = 'one'  #list is mutable
print(data)   #Answer = ['one', 2, 3, 4.0, 'five']


#Dict

contact = {'police':999, 'bomba':991}  # dict are key-value pairs

type(contact) 

contact['police']  #indexing, Answer = 999, show the pair value of the keyword

len(contact) #Answer = 2, length of keyword

contact['harry'] = 1234567
contact.keys()
contact.values()


#Tuple

red = (255,0,0)
red[0]  #Answer = 255
red[0:3] #Slicimg, answer = (255,0,0) , starting from 0 location until 3 steps from it

red[0] = 1 #Error


#Strings

myname = 'Jon\n'  #string with escapa character
print(myname)

myname.strip()  #strip \n, leading and ending

greet = f'Hello {myname}' #simple formatting
greet

msg = '{a} + {b} + {c}'.format(a=1,b=20,c=21) #another way to format string
msg

myname.upper() #capital Letter

myname.isalpha() #Answer = false




