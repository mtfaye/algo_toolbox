class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_lenght = 0 
        count = {}
        
        anchor = 0 
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            
            while (i - anchor + 1) - max(count.values()) > k:
                count[s[anchor]] -= 1
                anchor += 1
            max_lenght = max(max_lenght, i - anchor + 1)
            
        return max_lenght
