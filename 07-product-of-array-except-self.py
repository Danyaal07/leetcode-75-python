class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n  
        
        leftProduct = 1
        i = 0
    
        while i < n:
            answer[i] = leftProduct
            leftProduct *= nums[i]
            i += 1
        
        rightProduct = 1
        i = n - 1
        
        while i >= 0:
            answer[i] *= rightProduct
            rightProduct *= nums[i]
            i -= 1
        
        return answer