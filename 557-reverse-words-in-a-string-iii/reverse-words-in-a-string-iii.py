class Solution:
    def reverseWords(self, s: str) -> str:
        result=[]
        words = s.split(' ') 
        for i in words:
            reversed_words = i[::-1]
            result.append(reversed_words)# Reverse the list of words
        return ' '.join(result)  # Join the reversed words with a space

            