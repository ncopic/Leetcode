class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        #--------------------------------------------------------
        # Solution 1 - loop thru and remove all elements & get indicies 
        #--------------------------------------------------------
        '''
        remove_me = [] #keep track of what indicies need to get removed
        for ii in range(len(nums)):
            if nums[ii] == val:
                remove_me.append(ii)
        
        #if you adjust nums during above loop, indicies get messy, so we remove stuff here from back to front.
        for index in remove_me[::-1]:
            nums.pop(index)
        return len(nums)
        '''

        #.remove() is an option instead of .pop() and then you don't need indicies
        #--------------------------------------------------------
        # Solution 2 - loop thru and remove all elements, but use .remove()
        #--------------------------------------------------------
        how_many_to_remove = nums.count(val)
        for ii in range(how_many_to_remove):
            nums.remove(val)
        return len(nums)