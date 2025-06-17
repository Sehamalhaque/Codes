class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                result = []
                for num in digits:
                    result.append(num)
                return result
            digits[i] = 0
            i -= 1
        new_digits = [1]
        for _ in range(n):
            new_digits.append(0)
        return new_digits
