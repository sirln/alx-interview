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
    primes[0] = primes[1] = False
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(limit + 1) if primes[i]]


def can_win(n, primes):
    '''
    Determine if a player can win a round of the game.
    '''
    for prime in primes:
        if n % (prime + 1) == 0:
            return False
    return True


def isWinner(x, nums):
    '''
    Determine the winner of multiple rounds of the game.
    '''
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        if can_win(n, primes):
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
