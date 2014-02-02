# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 02:24:07 2014

@author: doyung
"""
def x_and_y(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1
    
print x_and_y(1, 4)