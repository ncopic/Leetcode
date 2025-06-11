class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        #-------------------------------------------------------------------
        # Solution 1 - 
        #-------------------------------------------------------------------

        #go thru the nums array and store nums[0]*nums[1]*...nums[ii] in forward[ii]
        forward  = [0]*len(nums)
        #go thru the nums array and store nums[ii]*...nums[-2]*nums[-1] in backward[ii]
        backward = [0]*len(nums)
        #out[ii] = forward[ii-1] * backward[ii+1]
        out = [0]*len(nums)

        forward[0] = nums[0]
        backward[-1] = nums[-1]

        for ii in range(len(nums)-1):
            forward[ii+1] = forward[ii] * nums[ii+1]    
            backward[-2-ii] = backward[-1-ii] * nums[-2-ii]

        out[0]=backward[1]
        out[-1]=forward[-2]
        
        for ii in range(len(nums)-2):
            out[ii+1] = forward[ii]*backward[ii+2]
        #print(out)
        return out

        