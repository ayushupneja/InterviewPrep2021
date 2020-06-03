class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        out = nums[0]
        max1 = out
        min1 = out
        for i in range(1,len(nums)):
            num = nums[i]
            a = num*max1
            b = num*min1
            max1 = max(num, a,b)
            min1 = min(num, a,b)
            out = max(out,max1)
            print(min1)
            print(out)
        return out