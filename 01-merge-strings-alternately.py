class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newstr = ""
        count = 0
        while count < min(len(word1),len(word2)):
            letter1 = word1[count]
            letter2 = word2[count]
            newstr = newstr + letter1 + letter2
            count += 1
        if count < len(word2):
            newstr = newstr + word2[count:len(word2)]
        if count < len(word1):
            newstr = newstr + word1[count:len(word1)]
        return newstr