class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}

        total = roman_map[s[-1]]  # Start with the last character's value

        for i in range(len(s) - 2, -1, -1):
            curr = roman_map[s[i]]
            next_ = roman_map[s[i + 1]]
            if curr < next_:
                total -= curr
            else:
                total += curr

        return total
