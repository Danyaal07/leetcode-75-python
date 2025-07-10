class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                leftCheck = (i == 0 or flowerbed[i - 1] == 0) 
                rightCheck = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                if leftCheck and rightCheck:
                    flowerbed[i] = 1
                    n -= 1
            if n <= 0:
                return True
        return False