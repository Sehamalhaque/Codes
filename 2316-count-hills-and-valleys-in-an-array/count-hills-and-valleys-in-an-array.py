from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Step 1: Remove consecutive duplicates
        compressed = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                compressed.append(nums[i])
        
        # Step 2: Count hills and valleys
        count = 0
        for i in range(1, len(compressed) - 1):
            if compressed[i-1] < compressed[i] > compressed[i+1]:  # Hill
                count += 1
            elif compressed[i-1] > compressed[i] < compressed[i+1]:  # Valley
                count += 1
        
        return count
