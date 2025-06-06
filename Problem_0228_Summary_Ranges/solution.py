class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #-------------------------------------------------------------------
        # Solution 1 - 
        #-------------------------------------------------------------------

        #edge case of len 0 or 1
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        out = [] #output list
        temp = [] #temp var used for formatting
        first = 0 #keeps track of the first index for a new set of numbers
        
        for ii in range(len(nums)-1):    
            if nums[ii+1]-nums[ii] == 1: #if the difference is 1, keep going until it isnt'
                pass
            elif (nums[first] == nums[ii]): #if it's the same number, we don't want "->" added to the output
                out.append(str(nums[ii]))
                first = ii + 1
            else: #if the difference between numbers is 2+, then update the output list
                temp = [str(nums[first]), str(nums[ii])]
                out.append("->".join(temp))
                first = ii + 1

        #handling final element in list
        if nums[-1]-nums[-2] == 1:
            temp = [str(nums[first]), str(nums[-1])]
            out.append("->".join(temp))
        else:
            out.append(str(nums[-1]))

        return out