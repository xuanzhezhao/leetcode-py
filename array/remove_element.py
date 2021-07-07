from typing import List
"""Leetcode Question 27:https://leetcode-cn.com/problems/remove-element/"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,n = 0,len(nums)
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i



if __name__ == '__main__':
    solution = Solution()
    #assert solution.search([2, 7, 11, 15], 15) == 3
    nums = [2, 7, 11, 15]
    val = 7
    print(solution.removeElement(nums, val))
    print(nums)


