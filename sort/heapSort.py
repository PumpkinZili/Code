class solution():

    def shiftHeap(self,nums, n,i):
        '''
        调堆，将num[i]沉下去，沉到不能再沉
        :param nums:
        :param n:
        :param i:
        :return:
        '''
        j = i*2 + 1
        while j<=n:
            if j+1 <= n and nums[j] < nums[j+1]:
                j += 1
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
            i, j = j, j*2 + 1

    def heapSort(self, nums):

        ##### 建堆，从后往前调整每一个非叶子节点
        for i in range(len(nums)//2, -1, -1):
            self.shiftHeap(nums, len(nums)-1, i)

        ##### 将堆顶元素取出，与末尾元素互换，再调整堆
        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.shiftHeap(nums, i-1, 0)

nums = [3,4,2,7,67,89,0,46,1,3]
solution().heapSort(nums)
print(nums)