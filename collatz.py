# Tyler Witt
# 6.27.14
# collatz.py
# ver 1.0

# This is a python function used to analyze the Collatz algorithm.

def collatz(uIn):
  num = uIn
  step = 0
  while num != 1:
    if num % 2 == 0:
      num = num / 2
    else:
      num = num * 3 + 1
    step = step + 1
  return step
