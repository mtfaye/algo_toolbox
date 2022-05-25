# Space = O(1)
# Time = O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        anchor = 0
        charSet = set()
        max_lenght = 0
        
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[anchor])
                anchor += 1
            charSet.add(s[i])
            max_lenght = max(max_lenght, i-anchor+1)
        
        return max_lenght
    
