class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        larr = [None]*len(nums)
        rarr = [None]*len(nums)
        out = [None]*len(nums)
        larr[0] = 1
        rarr[len(nums)-1] = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                larr[i] = nums[i-1] * larr[i-1]
        for j in range(len(nums)):
            if j == 0:
                continue
            else:
                rarr[len(nums)-j-1] = nums[len(nums)-j]*rarr[len(nums)-j]
        for k in range(len(nums)):
            out[k] = rarr[k]*larr[k]
        return out