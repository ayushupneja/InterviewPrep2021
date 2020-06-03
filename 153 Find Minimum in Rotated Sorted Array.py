class Solution:
    def findMin(self, nums: List[int]) -> int:
        prev = nums[0]
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num < prev:
                return num
            else:
                prev = num
        return nums[0]