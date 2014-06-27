# Tyler Witt
# findPrimes.py
# 6.27.14
# ver 1.0

# This function implements the Sieve of Eratosthenes algorithm to find all the prime numbers below lim

def findPrimes(lim):
  primes = []
  cur = 0
  if lim < 2:
    return None
  for num in range(2, lim + 1):
    primes.append(num)
  while (primes[cur] ** 2 < lim):
    for val in primes:
      if val % primes[cur] == 0 and val != primes[cur]:
        primes.remove(val)
    cur += 1
  return (primes)
