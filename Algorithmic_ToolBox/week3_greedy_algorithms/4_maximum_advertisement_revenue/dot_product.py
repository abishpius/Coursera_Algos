#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    n = 3
    a = [1, 3, -5]
    b = [-2, 4, 1]
    print(max_dot_product(a, b))
    
