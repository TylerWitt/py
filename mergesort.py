# Tyler Witt
# 6.27.14
# mergesort.py
# ver 1.0

# This file contains the algorithm for mergesort, which recursively divides
# a list into single elements, and then combines them back together in order.

def mergeSort(list1):
  if len(list1) < 2:
    return list1
  result = []
  mid = int(len(list1)/2)
  l = mergeSort(list1[:mid])
  r = mergeSort(list1[mid:])
  li = 0
  ri = 0
  while len(l) > li and len(r) > ri:
      if (l[li] < r[ri]):
        result.append(l[li])
        li += 1
      else:
        result.append(r[ri])
        ri += 1
  result += l[li:]
  result += r[ri:]
  return result
