class NewClass:
  pass
  def __init__(self):
    pass
  def __str__(self):
    pass
  def __print__(self):
    pass
  def __rsquare__(self):
    pass

  
def validPalindrome(strng: str) ->bool:
  def isPlalindrome(new_strng):
    left=0
    right=len(new_strng)-1
    
    while left < right:
      if new_strng[left]!=new_strng[right]:
        return False
      else:
        left+=1
        right-=1
      return True
    
  for i in range(len(s)):
    forward = s[:i] + s[i+1:]
  for j in range(len(S), 0, -1):
    backward = s[:j] + s[j+1:]
    
  return isPalindrome(forward) or isPalindrome(backward)

    
    
    
    
__main__==__name__:
 def main():
  pass
