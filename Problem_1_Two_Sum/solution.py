class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

#--------------------------------------------------------
# Try 1 - Brute force
#--------------------------------------------------------

        ''' 
        #Runs forever and times out
        ii = 0
        for ii in range(len(nums)):
            #print("ii loop: ",ii)
            for jj in range(len(nums)):
                #print("jj loop: ",jj)
                print("ii=",ii," jj=",jj)
                if target == int(nums[ii]) + int(nums[jj]):
                    if ii != jj and jj> ii:
                        return [ii,jj]
                #else:
                #    print("miss")
        '''

#--------------------------------------------------------
# Try 2
#--------------------------------------------------------
        '''
        #Runs in about 1000-1100 ms due to the nums_dict.keys() call that is made. Changing this to nums_dict reduces time to a handful of ms. 
        
        
        nums_dict = {}
        for ii in range(len(nums)):
            nums_dict.update({nums[ii]:ii}) #Fill up hash table with all values from input list and corresponding position

        counter = -1
        for possible_match in nums:
            counter = counter + 1
            x = target - possible_match #if 2 nums have to sum to the target num, then subtacting a possible match from the target would leave us with the other number to be summed
            if x in nums_dict.keys(): #check if the other number to sum is a key in the dictionary
                if counter != nums_dict[x]: #ensure that we didn't just pull the same number twice
                    return [counter, nums_dict[x]]
        '''
#--------------------------------------------------------
# Try 3
#--------------------------------------------------------

        #Trying to understand what makes runs 2 and 4 so different in terms of run time.
        #trying to optomize try 2.
        #Currently  runs in about 3 ms if we change the "nums_dict.keys()" to "nums_dict"
        #if we go back to try2 and change the "nums_dict.keys()" to "nums_dict" then it runs in ~6ms. 
        #Takeaway here is nums_dict.keys() is slow AF
        
        nums_dict = {}
        for ii in range(len(nums)):
            nums_dict.update({nums[ii]:ii})

        for ii in range(len(nums)):
            x = target - nums[ii]
            if x in nums_dict: #"if x in nums_dict.keys():" has a run time of ~1000ms. Where as "if x in nums_dict" has runtime of ~3ms
                if ii != nums_dict[x]:
                    return [ii, nums_dict[x]]

        
#---------------------------------------------------------------------------------------
# Try 4 - online solution that runs in 0ms - https://www.youtube.com/watch?v=aRE7Nxb3Qfs
#---------------------------------------------------------------------------------------
        '''
        h = {}
        for ii in range(len(nums)):
            h[nums[ii]] = ii

        for ii in range(len(nums)):
            y = target - nums[ii]
            if y in h and h[y] != ii:
                return [ii, h[y]]
        '''