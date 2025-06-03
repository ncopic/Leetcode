class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        #-------------------------------------------------------------------
        # Solution 1 - State Machine: Assumes all ints in matrix are unique.
        #-------------------------------------------------------------------
        #if the matrix is empty
        '''
        if not matrix:
            return None

        m_len = len(matrix[0]) #jj max index value
        n_len = len(matrix) #ii  max index value
        ii = 0
        jj = 0
        direction = "Right" #Right->Down->Left->Up
        out = []

        while(len(out) != (m_len * n_len)): #loop until all elements in orignal matrix have been added to the output array
            out.append(matrix[ii][jj])
            print(out)
            if direction == "Right":
                #If we're at max jj index, or if next right element is already in output list, switch to going down.
                if (jj == m_len-1) or (matrix[ii][jj+1] in out):
                    direction = "Down"
                    ii = ii + 1
                else: #keep going right
                    jj = jj + 1
            elif direction ==  "Down":
                #if at max ii index; or next ii index is already in out array
                if (ii == n_len-1) or (matrix[ii+1][jj] in out):
                    direction = "Left"
                    jj = jj - 1
                else:
                    ii = ii + 1
            elif direction == "Left":
                #if at the left most elements, go up
                if (jj == 0) or (matrix[ii][jj-1] in out):
                    direction = "Up"
                    ii = ii - 1
                else:
                    jj = jj - 1
            elif direction == "Up":
                if (matrix[ii-1][jj] in out):
                    direction = "Right"
                    jj = jj + 1 
                else:
                    ii = ii - 1 
        return out
        '''         
        #-----------------------------------------------------------------------
        # Solution 2 - State Machine: Assumes all ints in matrix are NOT unique.
        #-----------------------------------------------------------------------
        #if the matrix is empty
        if not matrix:
            return None

        m_len = len(matrix[0]) #jj max index value
        n_len = len(matrix) #ii  max index value
        jj_walk_right = m_len - 1
        ii_walk_down = n_len - 1
        jj_walk_left = 0
        ii_walk_up = 1 #starts at 1 cuz first time headed up always bumps into 1st element in spiral
        ii = 0
        jj = 0
        direction = "Right" #Right->Down->Left->Up
        out = []

        while(len(out) != (m_len * n_len)): #loop until all elements in orignal matrix have been added to the output array
            out.append(matrix[ii][jj])
            if direction == "Right":
                #If we're at max jj index, or if next right element is already in output list, switch to going down.
                if jj == jj_walk_right:
                    direction = "Down"
                    jj_walk_right = jj_walk_right - 1
                    ii = ii + 1
                else: #keep going right
                    jj = jj + 1
            elif direction ==  "Down":
                #if at max ii index; or next ii index is already in out array
                if ii == ii_walk_down:
                    direction = "Left"
                    ii_walk_down = ii_walk_down - 1
                    jj = jj - 1
                else:
                    ii = ii + 1
            elif direction == "Left":
                #if at the left most elements, go up
                if jj == jj_walk_left :
                    direction = "Up"
                    jj_walk_left = jj_walk_left + 1
                    ii = ii - 1
                else:
                    jj = jj - 1
            elif direction == "Up":
                if ii == ii_walk_up:
                    direction = "Right"
                    ii_walk_up = ii_walk_up + 1
                    jj = jj + 1 
                else:
                    ii = ii - 1 
        return out
                    
