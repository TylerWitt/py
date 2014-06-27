# Tyler Witt
# closestPair.py
# 6.27.14
# ver 1.0

# This set of functions can be used to find the closest two points in an array of points.
# Returns None on a list too short.

# Restrictions: The algorithm used for findPair will not count pairs with the same values,
#   For example: if the input were (1,1), (2,2), (2,2), the pairs returned would be (1,1), (2,2).

def distance(pt1, pt2):
  return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**(1/2)

def findPair(ptList):
  if len(ptList) > 1:
    shortest = None
    for curPt in ptList:
      for evalPt in ptList:
        if curPt != evalPt:
          ptDist = distance(curPt, evalPt)
          if shortest == None or ptDist < shortest:
            shortest = ptDist
            points = [curPt, evalPt]
  else:
    points = None
  return points
