#!/usr/bin/python3
"""A method that calculates the fewest number of operations needed to result
in exactly n H characters in the file"""


def minOperations(n):
    """Computes the fewest number of operations needed to result in exactly
    n H characters
    """
    if n <= 1:
        return 0

    # Initialize an array to store the minimum number of operations
    dp = [0] * (n + 1)

    # Iterate from 2 to n
    for i in range(2, n + 1):
        dp[i] = i  # Initialize with maximum possible operations

        # Find the divisor of i which gives a remainder of 0
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                # Calculate the number of operations required to reach i
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
