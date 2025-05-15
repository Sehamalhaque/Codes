class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i, n1 in enumerate(num1):
            carry = 0
            for j, n2 in enumerate(num2):
                total = res[i + j] + int(n1) * int(n2) + carry
                res[i + j] = total % 10
                carry = total // 10
            if carry:
                res[i + len(num2)] += carry
        
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
        return ''.join(map(str, res[::-1]))

        