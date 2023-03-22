#!/usr/bin/env python3

import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorize(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return i, n // i
    return None, None

if len(sys.argv) != 2:
    print("Usage: rsa <file>")
    sys.exit(1)

filename = sys.argv[1]
try:
    with open(filename) as f:
        n = int(f.readline().strip())
        p, q = factorize(n)
        if p is None:
            print(f"Error: {n} is not factorizable into two prime numbers")
        else:
            print(f"p={p}\nq={q}")
except FileNotFoundError:
    print(f"Error: file '{filename}' not found")
    sys.exit(1)

