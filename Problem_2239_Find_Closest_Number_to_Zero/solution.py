class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #-------------------------------------------------------------------
        # Solution 1 - Assume unsorted Array
        #-------------------------------------------------------------------

        closest = nums[0] #closet value in array is going to be the first value.

        for item in nums:
            if abs(item) < abs(closest): #if the item we're looking at is smaller than any we've found so far
                closest = item
            elif abs(item) == abs(closest) and item > closest: #if they have the same abs() value and the new one is bigger than the old one we found
                closest = item
            else:
                continue
        return closest





