class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set(nums)
        if len(unique_elements) == len(nums):
            return False
        else :
            return True

        