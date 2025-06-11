class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        #--------------------------------------------------------
        # Solution 1 - sort list by first interval
        #--------------------------------------------------------

        if len(intervals) == 1:
            return intervals
        
        #Key to this problem is to sort the list by the first element.
        #intervals.sort(key=lambda intervals: intervals[0])  # sorts in place
        sort = sorted(intervals, key=lambda intervals: intervals[0] )

        print(sort)
        out = []
        ii = 0
        
        for ii in range(len(sort)): #for every item in list
            if (not out):#if list is empty, add the first element
                out.append(sort[ii])
            elif out[-1][1] < sort[ii][0]: #if 4 in [1,4] is smaller than 6 in [6,7], then they aren't continuous. Add a new elmenet. 
                out.append(sort[ii])
            elif out[-1][1] < sort[ii][1] : #if 4 in [1,4] is smaller than 2 in [2,7], then update 4 to be 7. Range should be [1,7] 
                out[-1][1] = sort[ii][1]
        return out



     