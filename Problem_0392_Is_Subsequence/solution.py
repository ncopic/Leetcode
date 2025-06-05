class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #-------------------------------------------------------------------
        # Solution 1 - 
        #-------------------------------------------------------------------
        if len(s) == 0: #if it's an empty string, it'll match anything, even an empty t
            return True
        if not t: #if t is empty, there's not gonna be a match if S has anything in it
            return False
        if len(s)>len(t): #if s is longer than t, it can't be a substring
            return False
        if (len(s) == len(t)) and s[0] != t[0]: #if they're the same length and the first element doesnt match, return false
            return False

        jj_count = 0 #order matters, so this will keep track of how far into t we are looking, so we don't re-search t for letters
        matched_letters = 0 #keep track of how many matched letters we found. If it's the length of S, then S matched t for substring. 
        for ii in range(len(s)):
            for jj in range((len(t) - jj_count)):
                #print("jj: " + str(jj) + " jj_count: " + str(jj_count) + " total: " + str(jj+jj_count))
                if s[ii] == t[jj_count + jj]:
                    #print(s[ii] + t[jj_count + jj])
                    matched_letters = matched_letters + 1
                    jj_count = jj + jj_count
                    break
            jj_count = jj_count + 1
        return len(s) == matched_letters