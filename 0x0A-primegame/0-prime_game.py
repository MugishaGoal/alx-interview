#!/usr/bin/python3
"""determine who the winner of each game is"""


def sieve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_list = []
    for p in range(2, n + 1):
        if is_prime[p]:
            prime_list.append(p)
    return prime_list

def simulate_game(n, primes):
    available = [True] * (n + 1)
    turn = 0  # 0 for Maria, 1 for Ben
    
    while True:
        move_made = False
        for prime in primes:
            if prime <= n and available[prime]:
                move_made = True
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False
                break
        if not move_made:
            return 1 - turn  # the other player wins
        turn = 1 - turn

def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n, primes)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return None

