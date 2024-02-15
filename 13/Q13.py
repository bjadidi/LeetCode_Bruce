class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {"I":1, "V": 5, "X":10, "L":50, "C":100,"D":500,"M":1000}
        num = 0
        for index in range (0,len(s)-1):
            
            if symbols[s[index]] >= symbols[s[index+1]]:
                num += symbols[s[index]]
            else:
                num -= symbols[s[index]]
        return num + symbols[s[-1]]


        