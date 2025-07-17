class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars=[]
        for c in s:
            if c.isalnum():
                filtered_chars.append(c.lower())
        return filtered_chars == filtered_chars[::-1]
            