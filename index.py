# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 17:51:28 2021

@author: HP
"""

import random

comp=random.randint(1, 10)
attempt=1
me=int(input("guess number"))
while(True):
    if(me>comp):
        me=int(input("guess other no..the no is too big "))
        attempt += 1
    elif(me<comp):
         me=int(input("guess other no..the no is too small"))
         attempt+=1
    else:
     print("you guess the write no......")
     break 
            
        
