from typing import List
"""Leetcode Question 977: https://leetcode-cn.com/problems/squares-of-a-sorted-array/"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        k = j
        result = [0] * len(nums)
        while i<=j:
            if nums[i]*nums[i]<nums[j]*nums[j]:
                result[k] = nums[j]*nums[j]
                j = j-1
            else:
                result[k] = nums[i]*nums[i]
                i = i+1
            k = k - 1

        return result

if __name__ == '__main__':
    solution = Solution()
    #A simple test
    print(solution.sortedSquares([-7, -2, 1,7,11, 15]))