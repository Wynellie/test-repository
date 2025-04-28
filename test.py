from typing import *
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        length = len(nums)
        res = 0
        while r < length:
            while k:
                if not nums[r]:
                    k -= 1
                r += 1
            res = max(r-l,res)
            while not k:
                if not nums[l]:
                    k += 1
                l += 1
        return res

print(Solution().longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))