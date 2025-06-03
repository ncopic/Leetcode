class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

#--------------------------------------------------------
# Solution 1 - Simple Solution
#--------------------------------------------------------
        '''
        #Try1: slow way to do this
        prefix = strs[0]

        for ii in range(len(strs)): #go thru all words in the input list
            match_len = 0
            for jj in range(len(strs[ii])): #for each item in a list, look at each letter 
                if (jj < len(prefix)) and (prefix[jj] == strs[ii][jj]):#Make sure  index ins't out of range & check if the letters are the same between the prefix and word we're looking at
                        match_len = match_len + 1
                else: 
                    break
            prefix = prefix[:match_len]
            if len(prefix) == 0:
                 return prefix
        return prefix
       '''
#--------------------------------------------------------
# Solution 2 - sorted list
#--------------------------------------------------------        
        #if you sort the incoming list first, you can just look at the first and last word and see how much they have in common
        sorted_strs = sorted(strs)
        first = sorted_strs[0]
        last = sorted_strs[-1]
        prefix = ""

        for ii in range(len(first)):#loop thru each letter in the first word
            if (ii < len(last)) and first[ii] == last[ii]:#protect against out of index error AND check that the letters match between first/last word
                prefix = prefix + last[ii]
            else: #if you ever stop matching, we're done
                break
        return prefix