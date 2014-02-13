# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:52:54 2014

@author: pruvolo
"""

def get_primes(n):
    """ Returns a list of all prime integers in the range [1,n] """
    return_val = []
    isPrime = True

    for i in range(2,n+1):
        for j in range(2,i):
            print "i:", i, "j:", j, "i % j", i % j
            if i % j == 0:
                isPrime = False
                break
            else:
                isPrime = True
            print isPrime
        if isPrime:
            return_val.append(i)
            print "return_val", return_val
    return return_val


if __name__ == '__main__':
    print get_primes(7)
