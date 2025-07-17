class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letter=[]
        for i in s:
            if i.isalpha():
                letter.append(i)
        final=[]
        for i in s:
            if i.isalpha():
                final.append(letter.pop())
            else:
                final.append(i)
        return ''.join(final)

                


            