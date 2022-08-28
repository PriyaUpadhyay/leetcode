class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        dict = defaultdict(list)
        # as i-j for each diagonal is same so we storing values of
        # that diagonal in dict and 
        # (i-j) will be the key and 
        # value will be the list of values in that diagonal.
        for i in range(rows):
            for j in range(cols):
                dict[i-j].append(mat[i][j])
                
        # sorting the values in dict so that
        # the last element will be the smallest 
        # and can be popped out and placed in matrix in sorted order.        
        for key in dict:
            dict[key].sort(reverse=True)
        
        # placing the values back in original matrix.
        for i in range(rows):
            for j in range(cols):
                mat[i][j]= dict[i-j].pop()
                
        return mat        

                
                
                 
        
