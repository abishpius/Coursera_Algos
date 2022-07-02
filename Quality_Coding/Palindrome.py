# Helper Functions

def reverse_string(s: str) -> str:
  """
  Returns a reversed string.
  """
  rev = ''
  for ch in s:
    rev = ch +rev

  return rev

# Method 1
def is_palindrome1(s: str) -> bool:
  """
  Returns True if s is a palindrome.

  Method: reverse string and compare
  """
  rev = reverse_string(s)
  return s == rev

# Method 2
def is_palindrome2(s: str) -> bool:
  """
  Returns True if s is a palindrome.

  Method: reverse compare first and second half of string reversed
  """
  n = len(s)
  return s[:n//2] == reverse_string(s[n-n//2:])

# Method 3
def is_palindrome3(s: str) -> bool:
  """
  Returns True if s is a palindrome.

  Method: using two pointers 
  """
  first = 0
  last = len(s) - 1

  while first < last and s[first] == s[last]:
    first += 1
    last -= 1
  
  return last <= first

### Test ###
print('racecar')
print(is_palindrome1('racecar'))
print(is_palindrome2('racecar'))
print(is_palindrome3('racecar'))

print('dented')
print(is_palindrome1('dented'))
print(is_palindrome2('dented'))
print(is_palindrome3('dented'))