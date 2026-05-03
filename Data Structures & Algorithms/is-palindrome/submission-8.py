class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs=''.join(char.lower() for char in s if char.isalnum())
        for i in range(len(cs)):
            j=len(cs)-i-1
            if cs[i]!=cs[j]:
                return False
        return True

            
        