#!/usr/bin/python3
"""
Determines game winner based on prime numbers in rounds
"""


def sieve_of_eratosthenes(n):
    """
    Helper function to find all prime numbers up to n using
    the Sieve of Eratosthenes
    """
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


def isWinner(x, nums):
    """
    Determine the winner of each round and return the
    player with the most wins
    """
    if not nums or x < 1:
        return None

    # Find maximum number in nums to compute primes up to that number
    max_n = max(nums)
    primes_up_to_max = sieve_of_eratosthenes(max_n)

    # List to store the number of prime numbers up to each number i
    prime_count = [0] * (max_n + 1)

    # Calculate the cumulative number of primes up to each number
    for i in range(2, max_n + 1):
        prime_count[i] = prime_count[i - 1]
        if i in primes_up_to_max:
            prime_count[i] += 1

    # Initialize wins for each player
    maria_wins = 0
    ben_wins = 0

    # Evaluate each round
    for n in nums:
        # The number of primes up to n determines
        # the number of turns in the game
        if prime_count[n] % 2 == 0:
            # If the number of primes is even, Ben wins
            ben_wins += 1
        else:
            # If the number of primes is odd, Maria wins
            maria_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
