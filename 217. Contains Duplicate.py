from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new = set(nums)
        if len(nums)==len(new):
            return False
        else:
            return True
        