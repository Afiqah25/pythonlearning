# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:30:43 2023

@author: AfiqahHasbullah
"""

"""
Progress Bar
"""

import time
import sys

mylist = range(100)
length = float(len(mylist))

for i in mylist:
    time.sleep(0.1)
    progress = (i+1)/length
    prog_bar = '#' * int(progress * 50)
    prog_pct = int(progress * 100)
    msg = "\rInstalling : [%s] %d%%" %(prog_bar, prog_pct)
    sys.stdout.write(msg)
    sys.stdout.flush()
    
sys.stdout.write("\Installing : [%s] Done."  %(prog_bar))
sys.stdout.flush()