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
        # Solution 2 - Hash table??
        #--------------------------------------------------------

        dl = {}
        for ii in range(len(nums)):
            dl[nums[ii]] = ii

        x=int(len(dl))
        print("x = " + str(x))
        print(type(x))
        return x