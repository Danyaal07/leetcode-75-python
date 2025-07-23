class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        word = ''
        sentence = []
        newStr = ''
        s = ' '.join(s.split())
        for i in range(len(s)):
            if s[i] != " ":
                word = word + s[i]
            else:
                sentence.append(word)
                word = ''
        sentence.append(word)
        for i in range(len(sentence)):
            newStr = newStr + sentence[len(sentence)-1-i] + " "
        return newStr.strip()
