class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result =[]
        maxNum = 0
        for i in range(len(candies)):
            if candies[i] > maxNum:
                maxNum = candies[i]

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxNum:
                result.append(True)
            else:
                result.append(False)
        return result