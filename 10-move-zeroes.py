class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        newNums = []
        zeroCount = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                newNums.append(nums[i])
            else:
                zeroCount += 1

        for i in range(zeroCount):
            newNums.append(0)

        for i in range(len(newNums)):
            nums[i] = newNums[i]
            
                
