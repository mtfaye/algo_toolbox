class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(new_s, left, right):
            while left<right:
                if new_s[left] != new_s[right]:
                    return False
                else:
                    left  +=1
                    right -=1
            return True
        
        i = 0
        j = len(s) - 1
        
        while i < j :
            if s[i] != s[j]:
                return isPalindrome(s, i, j-1) or isPalindrome(s, i+1, j)
            i +=1
            j -=1
        return True 
