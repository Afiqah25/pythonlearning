# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:17:21 2023

@author: AfiqahHasbullah
"""

"""
String are arrays of unicode characters
string literal - either single-quote or double quote
multi-line string - triple quote
"""

str1 = 'Hello, World!'
print(str1)                    #Answer = Hello, World!

str2  = "Howd'y , partner?"
print(str2)                  #Answer = Howd'y , partner?


str3 = 'Harry say: "Good!"'
print(str3)                  #Answer = Harry say: "Good!"


"""
Example of multistring
"""
str5 = '''This is a multi-line 
string, using triple-quote 
or single quote'''
print(str5)

str6 = 'This is a multi-line\nstring, using triple-quote\nor single quote'
print(str6)

"""
raw string : a string with many illegal character
"""

path_to_home = 'C:\\Users\\Users\\Desktop'
print(path_to_home)    #Answer = C:\Users\Users\Desktop

raw_path = r'C:\Users\Users\Desktop'
print(raw_path)        #Answer = C:\Users\Users\Desktop

description = r'Use escape \n character to create new line' 
print(description)

description