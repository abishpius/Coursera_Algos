# Uses python3
import sys

def get_change(m):
  cnt = 0
  while (m-10) >= 0:
    cnt+=1
    m = m-10
  while (m-5) >= 0:
    cnt+=1 
    m = m-5
  while (m-1) >= 0:
    cnt+=1
    m=m-1
    #write your code here
  return cnt

if __name__ == '__main__':
    m = int(sys.argv[1])
    print(get_change(m))
