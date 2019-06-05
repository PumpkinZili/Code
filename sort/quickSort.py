import sys
class solution():
    def partition(self, nums, head, tail):
        temp = nums[head]
        while head<tail:
            while nums[tail] >= temp and head<tail:
                tail -= 1
            nums[head], nums[tail] = nums[tail], nums[head]
            while nums[head] <= temp and head<tail:
                head += 1
            nums[head], nums[tail] = nums[tail], nums[head]
        nums[head] = temp
        return head

    def quickSort(self, nums, head, tail):
        if head < tail:
            p = self.partition(nums, head, tail)
            self.quickSort(nums, head, p-1)
            self.quickSort(nums, p+1, tail)

nums = [3,4,2,7,67,89,0,46,1,3]
solution().quickSort(nums, 0, len(nums)-1)
print(nums)