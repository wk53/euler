"""Project Euler - Problem 7.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import sqrt


def is_prime(n):
    """Return True if n is prime."""
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:  # factor found -> not prime
            return False
    return True


primes = []  # list to store generated primes
j = 2  # start with first prime

while len(primes) < 10001:
    if is_prime(j):
        primes.append(j)
    j += 1

print(primes[-1])  # 10001st prime
