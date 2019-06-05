class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i] + nums[i-1]
        return max(nums)