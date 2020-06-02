class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runsum = -999999999999999999999999999999
        maxrunsum = -99999999999999999999999999999999999
        for i in range(len(nums)):
            if nums[i] > runsum+nums[i]:
                runsum = nums[i]
                if runsum > maxrunsum:
                    maxrunsum = runsum
            else:
                runsum = runsum+nums[i]
                if runsum > maxrunsum:
                    maxrunsum = runsum
        return maxrunsum