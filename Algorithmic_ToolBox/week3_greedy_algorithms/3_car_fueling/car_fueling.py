# python3
import sys


def compute_min_refills(distance, tank, stops):
  numRefills, currentRefill = 0,0
  n = len(stops)-1
  stops.append(distance)

  while currentRefill <= n:
    lastRefill = currentRefill
    
    while (currentRefill <= n and (stops[currentRefill+1] - stops[lastRefill]) <= tank):
      currentRefill += 1
    if currentRefill == lastRefill:
      return -1
    if currentRefill <= n+1:
      numRefills +=1
  return numRefills
  

if __name__ == '__main__':
    d, m, _, stops = 10, 3, 4, [1,2,5,9]
    print(compute_min_refills(d, m, stops))
