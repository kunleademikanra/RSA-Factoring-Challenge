#!/usr/bin/env python3

import sys

def factorize(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None, None

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

filename = sys.argv[1]
try:
    with open(filename) as f:
        for line in f:
            n = int(line.strip())
            p, q = factorize(n)
            if p is None:
                print(f"{n} is prime")
            else:
                print(f"{n}={p}*{q}")
except FileNotFoundError:
    print(f"Error: file '{filename}' not found")
    sys.exit(1)
