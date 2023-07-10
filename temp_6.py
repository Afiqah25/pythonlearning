# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 22:35:45 2023

@author: AfiqahHasbullah
"""

"""
While Loop
"""

spot_player , next_player = 'Red' , 'Blue'
move_count = 1

while move_count < 100:
    move_count += 1 #without this, loop wont exist
    spot_player , next_player = next_player , spot_player
    print('update game status, count = %d'%move_count)

"""Answer is 
update game status, count = 2
update game status, count = 3
update game status, count = 4
update game status, count = 5
update game status, count = 6
update game status, count = 7
update game status, count = 8
update game status, count = 9
update game status, count = 10
update game status, count = 11
update game status, count = 12
update game status, count = 13
update game status, count = 14
update game status, count = 15
update game status, count = 16
update game status, count = 17
update game status, count = 18
update game status, count = 19
update game status, count = 20
update game status, count = 21
update game status, count = 22
update game status, count = 23
update game status, count = 24
update game status, count = 25
update game status, count = 26
update game status, count = 27
update game status, count = 28
update game status, count = 29
update game status, count = 30
update game status, count = 31
update game status, count = 32
update game status, count = 33
update game status, count = 34
update game status, count = 35
update game status, count = 36
update game status, count = 37
update game status, count = 38
update game status, count = 39
update game status, count = 40
update game status, count = 41
update game status, count = 42
update game status, count = 43
update game status, count = 44
update game status, count = 45
update game status, count = 46
update game status, count = 47
update game status, count = 48
update game status, count = 49
update game status, count = 50
update game status, count = 51
update game status, count = 52
update game status, count = 53
update game status, count = 54
update game status, count = 55
update game status, count = 56
update game status, count = 57
update game status, count = 58
update game status, count = 59
update game status, count = 60
update game status, count = 61
update game status, count = 62
update game status, count = 63
update game status, count = 64
update game status, count = 65
update game status, count = 66
update game status, count = 67
update game status, count = 68
update game status, count = 69
update game status, count = 70
update game status, count = 71
update game status, count = 72
update game status, count = 73
update game status, count = 74
update game status, count = 75
update game status, count = 76
update game status, count = 77
update game status, count = 78
update game status, count = 79
update game status, count = 80
update game status, count = 81
update game status, count = 82
update game status, count = 83
update game status, count = 84
update game status, count = 85
update game status, count = 86
update game status, count = 87
update game status, count = 88
update game status, count = 89
update game status, count = 90
update game status, count = 91
update game status, count = 92
update game status, count = 93
update game status, count = 94
update game status, count = 95
update game status, count = 96
update game status, count = 97
update game status, count = 98
update game status, count = 99
update game status, count = 100

"""


mylist = ['a' , 'b' , 'c']
for item in mylist:
    print(item)
    
"""Answer
a
b
c
"""