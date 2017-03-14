# -*- coding: utf8 -*-

def euc_iterative(a, b):
    """ Euclid´s algorithm implemented iteratively (with 'while'). """
    r_k0 = a
    r_k1 = b

    #The // operator returns the floor of the division.
    q = r_k0 // r_k1
    r_k2 = r_k0 % r_k1

    while r_k2 != 0:
        r_k0 = r_k1
        r_k1 = r_k2

        q = r_k0 // r_k1
        r_k2 = r_k0 % r_k1

    return r_k1

def euc_recursive(a, b):
    """ Euclid´s algorithm implemented recursively (calling the function within the function). """
    r_k0 = a
    r_k1 = b

    q = r_k0 // r_k1
    r_k2 = r_k0 % r_k1

    if r_k2 == 0:
        return r_k1

    return euc_recursive(r_k1, r_k2)

#You have to separate the 'getting data' part from the actual 'do something' part.
n1 = int(raw_input("a = "))
n2 = int(raw_input("b = "))

#The outputs should be the same...I hope :)
print(euc_iterative(n1, n2), euc_recursive(n1, n2)) 




