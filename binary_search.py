from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)-1
        left = 0

        while left <= right:
            #mid = int((right + left) / 2)
            mid = (left + right) // 2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == '__main__':
    solution = Solution()
    #assert solution.search([2, 7, 11, 15], 15) == 3
    print(solution.search([2, 7, 11, 15], 15))