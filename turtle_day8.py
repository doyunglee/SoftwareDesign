# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:41:21 2014

@author: doyung
"""
from swampy.TurtleWorld import *
from math import pi

def my_square():
    world = TurtleWorld()
    bob = Turtle()
    bottom_left_x = raw_input("Give us starting coordinates (x): ", )
    bottom_left_y = raw_input("Give us starting coordinates (y): ", )    
    square_length = raw_input("What's the length of the square?: ", )
    
    bottom_left_x = int(bottom_left_x)
    bottom_left_y = int(bottom_left_y)
    square_length = int(square_length)
    
    bob.x = bottom_left_x
    bob.y = bottom_left_y
    bob.heading = 0
    for i in range(4):
        bob.fd(square_length)
        bob.heading = bob.heading + 90

def my_regular_polygon(bottom_left_x, bottom_left_y, sides, polygon_length):
    world = TurtleWorld()
    bob = Turtle()       
    bob.delay = .01
    bob.x = bottom_left_x
    bob.y = bottom_left_y
    
    bob.heading = 0
    for i in range(sides+1):
        bob.fd(polygon_length)
        bob.heading = bob.heading + 360.0/sides
        
def my_circle():
    bottom_left_x = int(raw_input("Give us center coordinates (x): ", ))
    bottom_left_y = int(raw_input("Give us center coordinates (y): ", )) 
    radius = float(raw_input("What's the radius of the circle?: ", ))
    side_length = 2*pi*radius/100
    my_regular_polygon(bottom_left_x, bottom_left_y, 100, side_length)

world = TurtleWorld()
elsa = Turtle()
elsa.delay = 0.01
elsa.x = -150
elsa.y = -100
angle = 0
snowflake_side = 0
def snow_flake_side(turtle, l, level, angle):
    """ Draw a side of the snowflake curve with side length l and recursion depth of level """
    if level != 0:
        elsa.fd(l/2.0)
        snow_flake_side(elsa, l/3.0, level-1, angle)
        elsa.fd(l/2.0)        
        elsa.rt(60)
        
        elsa.fd(l/2.0)
        snow_flake_side(elsa, l/3.0, level-1, angle)
        elsa.fd(l/2.0)
        elsa.lt(120)
        
        elsa.fd(l/2.0)
        snow_flake_side(elsa, l/3.0, level-1, angle)
        elsa.fd(l/2.0)
        elsa.rt(60)
        
        elsa.fd(l/2.0)
        snow_flake_side(elsa, l/3.0, level-1, angle)
        elsa.fd(l/2.0)
    
if __name__ == '__main__':
    snow_flake_side(elsa,30,3,0)
    elsa.heading = 120
    snow_flake_side(elsa,30,3,0)
    elsa.heading += 120
    snow_flake_side(elsa,30,3,0)
