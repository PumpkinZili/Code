class solution():
    def selectionSort(self, nums):
        for i in range(len(nums)):
            m = i
            for j in range(i, len(nums)):
                if nums[j] < nums[m]:
                    m = j
            nums[i], nums[m] = nums[m], nums[i]

nums = [3,4,2,7,67,89,0,46,1,3]
solution().selectionSort(nums)
print(nums)