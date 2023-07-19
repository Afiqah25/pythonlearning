# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:42:08 2023

@author: AfiqahHasbullah
"""
"""
Use + for concatenation, * for repitition

"""

str1 = 'Hello, '
str2 = 'Harry Porter'
str3 = str1 + str2
print(str3)

str4 = 'I am ' + 'so '*5 + 'happy'
print(str4)


line = '-' *30
print(line)

for i in range(1,11) :
    progress_bar = '#'*i +'l' + str(i*10) + '%'
    print(progress_bar)
    
"""
String as an array of character
"""

#INdex and slice to obtain substring

s = 'string is an array'

s[0] #character at index = 0 , s

s[-1] #the 1st character from back of the string , y

s[0:6] #Answer = string

s[-5:] #the 5th character from the back, and move forward till end

