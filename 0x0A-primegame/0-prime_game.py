#!/usr/bin/python3


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None

    # Determine the maximum number to generate primes up to
    n = max(nums)

    # Sieve of Eratosthenes to generate prime numbers up to n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    # Prime counts up to each index
    prime_count = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    marias_wins, bens_wins = 0, 0

    # Determine the winner for each round
    for round_n in nums:
        if prime_count[round_n] % 2 == 1:
            marias_wins += 1
        else:
            bens_wins += 1

    # Determine the overall winner
    if marias_wins > bens_wins:
        return 'Maria'
    elif bens_wins > marias_wins:
        return 'Ben'
    else:
        return None
