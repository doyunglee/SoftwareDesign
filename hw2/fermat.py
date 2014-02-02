# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:20:24 2014

@author: doyung
"""

def check_fermat():
    a = raw_input( "Give me an 'a': ")
    b = raw_input( "Give me a 'b': ")
    c = raw_input( "Give me a 'c': ")
    n = raw_input( "Give me an 'n': ")
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    left = a**n + b**n 
    right = c**n
    if left == right and n > 2:
        print "wow, fermat was wrong!"
    else:
        print "No, that doesn't work. Sorry."
    
check_fermat()