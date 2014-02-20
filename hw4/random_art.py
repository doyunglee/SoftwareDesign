# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
import math

def build_random_function(min_depth, max_depth):
    """
    This function takes in a minimum depth and a maximum depth and will give you a function that 
    has a depth between the min and the max depth.
    """
    the_decider = randint(min_depth, max_depth)    
    if the_decider <=1: #base case of the recursion. 
        if randint(0,1) == 0:    
            return 'x'
        else:            
            return 'y'
    else:
        which_one = randint(0,6)
        if which_one == 0: #Product of a and b
            return ["prod",build_random_function(min_depth-1, max_depth-1),build_random_function(min_depth-1, max_depth-1)]
        elif which_one == 1: #sin(pi*a)
            return ["sin_pi",build_random_function(min_depth-1, max_depth-1)]
        elif which_one == 2: #cos(pi*a)
            return ["cos_pi",build_random_function(min_depth-1, max_depth-1)]
        elif which_one == 3: #a^3
            return ["3_pow", build_random_function(min_depth-1, max_depth-1)]
        elif which_one == 4: #if it's just x
            return build_random_function(min_depth-1, max_depth-1)
        elif which_one == 5: #if it's just y
            return build_random_function(min_depth-1, max_depth-1)
        else: #y = -x 
            return ["neg", build_random_function(min_depth-1, max_depth-1)]
            
        
def evaluate_random_function(f, x, y):
    """
    This function takes in the function, x and y values. It then calculates the value of the function
    using the x and y.
    """
    #f[0] is the beginning of the function. As it is sent back via recursion, the next value is used.
    if f[0] == "x":
        return x
    elif f[0] == "y":
        return y        
    elif f[0] == "prod":
        return evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y)
    elif f[0] == "sin_pi":
        return math.sin(math.pi*evaluate_random_function(f[1], x, y))
    elif f[0] == "cos_pi":
        return math.cos(math.pi*evaluate_random_function(f[1], x, y))
    elif f[0] == "3_pow":
        return evaluate_random_function(f[1], x, y) ** 3
    elif f[0] == "neg":
        return evaluate_random_function(f[1], x, y) * -1                  

     
def making_pictures():
    im = Image.new("RGB",(350,350)) #creates an image.
    trippy_art = im.load() #load the image
    
    red = build_random_function(20, 30) #creates function for the color red
    green = build_random_function(20,30) #creates function for the color green
    blue = build_random_function(20, 30) #creates function for the color blue
    for i in range(349):
        for j in range(349):
            i2 = (i / (349/2.0)) - 1#change the scale from [0, 349] to [-1, 1]
            j2 = (j / (349/2.0)) - 1
            red_eval = evaluate_random_function(red, i2, j2) #evaluates the red function
            green_eval = evaluate_random_function(green, i2, j2) #evaluates the green function
            blue_eval = evaluate_random_function(blue, i2, j2) #evaluates the blue function
            red_plot = (1 + red_eval)*(255/2.0) #change the scale from [-1, 1] to [0, 255]
            green_plot = (1 + green_eval)*(255/2.0)
            blue_plot = (1 + blue_eval)*(255/2.0)
            red_plot = int(red_plot) #pixels have to be integers, so let's change that.
            green_plot = int(green_plot)
            blue_plot = int(blue_plot)
            trippy_art[i, j] = (red_plot, green_plot, blue_plot) #THIS IS A GRID inputing each color into the plot.
    im.save('trippy_art.png')
    im.show()
            
if __name__ == '__main__':
    making_pictures()