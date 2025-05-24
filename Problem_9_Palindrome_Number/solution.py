class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
#--------------------------------------------------------
# Solution 1 - Simple Solution
#--------------------------------------------------------

        ''' 
        #quick return if statements
        if x < 0:
            return False
        
        if x < 10:
            return True
        
        y = str(x)
        if str(x) == y[::-1]:
            return True
        else:
            return False
        '''


#--------------------------------------------------------
# Solution 2 - not using strings in solution
#--------------------------------------------------------

        '''
        #quick return if statments
        if x < 0:
            return False
        
        if x < 10:
            return True
        
        og_num = x #original input number passed in
        up = 0 #unknown Palendrome
        while(x > 0):
            last_dig = x % 10
            up = (up * 10) + last_dig
            x = x/10
        if og_num == up:
            return True
        else:
            return False
        '''


#--------------------------------------------------------
# Solution 3 - Brute force fastest leetcode solution
#--------------------------------------------------------
        str_x = str(x)
        return str_x == str_x[::-1]
