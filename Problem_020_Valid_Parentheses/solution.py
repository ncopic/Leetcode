class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #--------------------------------------------------------
        # Solution 1 - Simple Solution
        #--------------------------------------------------------
        q = []
        d = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        for ii in range(len(s)):
            if s[ii] not in d: #check if ending bracket or beginning bracket
                q.append(s[ii]) #append beginning brackets to queue
            elif (len(q) > 0) and (d[s[ii]] == q[-1]): #if ending bracket, see if its pair is the latest in queue
                q.pop() #if they are the same sytle bracket, pop off cuz we know they pair off
            else:
                return False
        return len(q) == 0 #want to return True if we hit here, but also need to double check that the len of queue is 0.



