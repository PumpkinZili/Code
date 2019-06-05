class solution():
    def insertSort(self, nums):
        '''
        :param nums: list[nums]
        :return: sorted list[nums]
        '''
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
        return nums

nums = [3,4,2,7,67,89,0,46,1,3]

print(solution().insertSort(nums))
