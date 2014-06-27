# Tyler Witt
# bubble.py
# 6.27.14
# ver 1.0

# This is a bubble sort algorithm, with the swap function required.

def swap(list1, ind1, ind2):
  temp = list1[ind1]
  list1[ind1] = list1[ind2]
  list1[ind2] = temp
  return list1

def bubble(list1):
  bound = len(list1) - 1
  while (bound > 1):
    for i in range(bound):
      if (list1[i] > list1[i+1]):
        list1 = swap(list1, i, i+1)
    bound -= 1
  return list1
