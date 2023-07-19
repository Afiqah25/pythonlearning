# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 18:19:59 2023

@author: AfiqahHasbullah
"""

"""
String is iterable
"""

msg = 'Hello'

for c in msg:
    print(c)


for c in msg:
    print(c,end="")
    
"""
Formatting Strings

Other than direct concatenation, there are 3 possible ways :

    f-string
    format method
    % substitution
"""

fname = ['file1.txt' , 'file2.txt' , 'file3.txt' , 'file4.txt']

msg = 'Processing '+ fname[0] +'...[Done]\n'

msg =  msg + f'Processing {fname[1]}...[Done]\n'

msg = msg +   'Processing {f} ...[Done]\n'.format(f=fname[2]) 

msg = msg +   'Processing %s ...[Done]\n'%(fname[3])   
    
print(msg)
    


