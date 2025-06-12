class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        #-------------------------------------------------------------------
        # Solution 1 - 90 Degree rotate is 2 steps. 
        #-------------------------------------------------------------------
        # Step 1, flip across y=-x axis. 
        # Step 2, reverse matrix[ii] list.
        #-------------------------------------------------------------------
        
        #Step 1 - input is NxN, so no out of index concerns since len(matrix)==len(matrix[ii])
        for ii in range(len(matrix)):
            for jj in range(len(matrix[0])):
                if ii < jj:
                    break
                temp = matrix[ii][jj]
                matrix[ii][jj] = matrix[jj][ii]
                matrix[jj][ii] = temp
        
        #Step 2
        for ii in range(len(matrix)):
            matrix[ii] = matrix[ii][::-1]
        return