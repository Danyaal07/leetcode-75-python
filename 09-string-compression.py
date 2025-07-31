class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read = 0
        write = 0
        while read < len(chars):
            start = read
            read += 1
            while  read < len(chars) and chars[start] == chars[read]:
                read += 1
            chars[write] = chars[start]
            write += 1
            count = read - start
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write
