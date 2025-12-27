class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums.sort()
        triplets = set()
        for i in range(0,len(nums)-2):
            

            j = i + 1
            k = len(nums)-1
            
            target = -nums[i]

            while(j<k):
                current_sum = nums[j]+nums[k]
                

                if ((current_sum == target)):
                    triplets.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1

                    

                if ((current_sum > target)):
                    k-=1

                if ((current_sum < target)):
                    j+=1

              
        return list(triplets)
                