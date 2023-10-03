"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    primes = 2
    
    while len(list) != number_of_primes:
        prime = True
        for i in range (2, primes//2):
            if primes % i == 0:
                prime = False
        list.append(i)
    return list
