class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        #-------------------------------------------------------------------
        # Solution 1 - build string using strings
        #-------------------------------------------------------------------
        '''
        out_str = "" #output string
        append_me = 0 #which str to append if not the same length
        
        len1 = len(word1)
        len2 = len(word2)

        if len1 >= len2:
            counter = len2
            append_me = 1
        else:
            counter = len1
        
        for ii in range(counter): #alternate adding letters for the length of the smaller word
            out_str = out_str + word1[ii] + word2[ii]
        
        if len1 != len2: #append the end if they aren't the same length
            if append_me == 1:
                out_str = out_str + word1[ii+1:]
            else:
                out_str = out_str + word2[ii+1:]
            
        return out_str
        '''

        #-------------------------------------------------------------------
        # Solution 2 - build string using array and .join()
        #-------------------------------------------------------------------
        
        out_str = [] #output string
        append_me = 0 #which str to append if not the same length
        
        len1 = len(word1)
        len2 = len(word2)

        if len1 >= len2:
            counter = len2
            append_me = 1
        else:
            counter = len1
        
        for ii in range(counter): #alternate adding letters for the length of the smaller word
            out_str.append(word1[ii])
            out_str.append(word2[ii])
        
        if len1 != len2: #append the end if they aren't the same length
            if append_me == 1:
                out_str.append(word1[ii+1:])
            else:
                out_str.append(word2[ii+1:])
            
        return "".join(out_str) 