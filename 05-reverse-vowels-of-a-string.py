class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        newVowels = []
        pos = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        # Step 1: Find vowels and their positions
        for i in range(len(s)):  # fixed range
            if s[i] in vowels:   # no need to use .lower()
                newVowels.append(s[i])  # fixed: actually add the vowel
                pos.append(i)

        # Step 2: Reverse the vowels
        newVowels = newVowels[::-1]

        # Step 3: Rebuild the string with reversed vowels
        s_list = list(s)  # convert string to list for mutability
        for i in range(len(pos)):
            s_list[pos[i]] = newVowels[i]

        return ''.join(s_list)

