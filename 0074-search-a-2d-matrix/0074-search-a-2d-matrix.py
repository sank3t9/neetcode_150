class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = (m*n) - 1
        mid = (left+right)//2
        mid_value = matrix[mid//n][mid%n]

        while(left<=right):
            mid = (left+right)//2
            mid_value = matrix[mid//n][mid%n]

            if(target==mid_value):
                return True

            if(target>mid_value):
                left = mid + 1

            if(target<mid_value):
                right = mid - 1

        return False
            


        
        