from typing import List
"""Leetcode Question 209:https://leetcode-cn.com/problems/minimum-size-subarray-sum/"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 # The start of sliding window
        length = float("inf") #The length of target array
        sum = 0 # The sum of target array

        for right in range(len(nums)): #the end of sliding window
            sum = sum+nums[right]
            while sum>=target:
                length =min(length, right - left + 1)
                sum = sum - nums[left]
                left = left + 1
        if length == float("inf"):
            return 0
        else: return length


if __name__ == '__main__':
    solution = Solution()
    #Test
    print(solution.minSubArrayLen(15,[5,1,3,5,10,7,4,9,2,8]))