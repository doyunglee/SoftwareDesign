# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:47:14 2014

@author: doyung
"""

def grid():
    print "+ " + "- "*4 + "+ " + "- "*4 + "+"
    print "|" + " "*9 + "|" + " "*9 + "|"
    print "|" + " "*9 + "|" + " "*9 + "|"
    print "|" + " "*9 + "|" + " "*9 + "|"
    print "|" + " "*9 + "|" + " "*9 + "|"
    print "+ " + "- "*4 + "+ " + "- "*4 + "+"
    print "|" + " "*9 + "|" + " "*9 + "|"
    print "|" + " "*9 + "|" + " "*9 + "|"
    print "|" + " "*9 + "|" + " "*9 + "|"
    print "|" + " "*9 + "|" + " "*9 + "|"
    print "+ " + "- "*4 + "+ " + "- "*4 + "+"
    

def mid_line():
    print ("|" + " "*9 + "|" + " "*9 + "|" + " "*9 + "|" + " "*9 + "|")

def four_times(f):
    f()
    f()
    f()
    f()

def grid_big():
    print "+ " + "- "*4 + "+ " + "- "*4 + "+ " + "- "*4 + "+ " + "- "*4 + "+ "
    four_times(mid_line)

def grid_big_foreals():
    four_times(grid_big)
    print "+ " + "- "*4 + "+ " + "- "*4 + "+ " + "- "*4 + "+ " + "- "*4 + "+ "
    
grid_big_foreals()