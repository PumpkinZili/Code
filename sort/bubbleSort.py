class solution():
    def bubbleSort(self,nums):
        for i in range(len(nums)-1, 0, -1):
            for j in range(0, i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

nums = [3,4,2,7,67,89,0,46,1,3]
solution().bubbleSort(nums)
print(nums)