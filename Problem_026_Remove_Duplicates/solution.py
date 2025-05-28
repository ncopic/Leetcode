class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        #--------------------------------------------------------
        # Solution 1 - loop thru every element - slow solution
        #--------------------------------------------------------


        #--------------------------------------------------------
        # Solution 2 - Hash table shortcut
        #--------------------------------------------------------

        dl = {}
        for ii in range(len(nums)):
            dl[nums[ii]] = ii

        keys = sorted(dl.keys())
        for ii in range(len(keys)):
            nums[ii] = keys[ii]
        x=len(dl)
        return x