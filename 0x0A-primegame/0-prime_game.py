#!/usr/bin/python3
"""
Determines game winner based on prime numbers in rounds
"""


def isWinner(x, nums):
    """
    Determine the winner of each round and return the
    player with the most wins.
    """
    if not nums or x < 1:
        return None

    # Find maximum number to compute primes up to that number
    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    # Initialize prime_count array
    prime_count = [0] * (max_n + 1)

    # Sieve and prime count calculation in one loop
    for p in range(2, max_n + 1):
        if primes[p]:
            for multiple in range(p * p, max_n + 1, p):
                primes[multiple] = False

        # Update the prime count up to the current number `p`
        prime_count[p] = prime_count[p - 1] + (1 if primes[p] else 0)

    # Initialize win counts for both players
    maria_wins, ben_wins = 0, 0

    # Evaluate each round, only considering up to x rounds
    for n in nums[:x]:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
