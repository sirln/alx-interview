#!/usr/bin/python3
'''
Prime Numbers Game Module
'''


def sieve_of_eratosthenes(limit):
    '''
    Sieve of Eratosthenes algorithm to generate
    prime numbers up to a given limit.
    '''
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return primes


def count_primes(n):
    '''
    Count the number of prime numbers up to a given n.
    '''
    primes = sieve_of_eratosthenes(n)
    count = sum(1 for prime in primes if prime)
    return count


def isWinner(x, nums):
    '''
    Determine the winner based on whether the number
    of primes is even or odd.
    '''
    if x <= 0 or not nums:
        return None

    ben = 0
    maria = 0
    for num in nums:
        if count_primes(num) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif ben < maria:
        return "Maria"
    else:
        return None
