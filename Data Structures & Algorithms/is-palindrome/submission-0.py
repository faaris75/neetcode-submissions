class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n - 1

        while l < r:
            # Changed s(l) to s[l]
            if not s[l].isalnum():
                l += 1
                continue
            # Changed s(r) to s[r]
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True