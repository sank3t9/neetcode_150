class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def time_taken(speed):
            
            total_hrs = 0
            for bananas in piles:
                total_hrs += math.ceil(bananas/speed)

            return total_hrs


        left = 1
        right = max(piles)
        answer = -1
        
        while(left < right):
            mid = (left+right)//2

            if (time_taken(mid) <= h):
                right = mid
            if (time_taken(mid) > h):
                left = mid + 1

        return right
            

        
        
            


        