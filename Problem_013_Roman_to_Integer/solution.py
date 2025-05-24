class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

#--------------------------------------------------------
# Solution 1 - Simple Solution
#--------------------------------------------------------

        convert_total = 0
        lookup = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        for ii in range(len(s)-1):
            curr_symbol = (s[ii])
            next_symbol = (s[ii+1])

            #see if the current symbol is bigger or smaller than the next symbol
            if lookup[curr_symbol] < lookup[next_symbol]:#if smaller do subtraction
                convert_total = convert_total - lookup[curr_symbol]
            else:#do addition
                convert_total = convert_total + lookup[curr_symbol]

        convert_total = convert_total + lookup[s[-1]] #always add the final num
        return convert_total