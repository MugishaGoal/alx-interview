#!/usr/bin/python3
"""Determine who the winner of each game is"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds"""
    if x < 1 or not nums:
        return None

    def sieve(max_n):
        is_prime = [True] * (max_n + 1)
        p = 2
        while p * p <= max_n:
            if is_prime[p]:
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, max_n + 1) if is_prime[p]]

    # Initialize variables to keep track of wins
    maria_wins, ben_wins = 0, 0

    # Precompute primes up to the maximum value in nums
    max_n = max(nums)
    primes = sieve(max_n)

    for n in nums:
        primes_count = sum(1 for prime in primes if prime <= n)
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
