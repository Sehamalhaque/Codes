from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        total = 0

        for num in nums:
            if num > 0 and num not in seen:
                total += num
                seen.add(num)

        # If no positive numbers, pick max number (negative or zero)
        if total == 0:
            return max(nums)
        return total
