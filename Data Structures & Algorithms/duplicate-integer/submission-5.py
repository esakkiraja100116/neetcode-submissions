class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        source = dict()
        for i in nums:
            if i in source:
                return True
            source[i] = True

        return False 

        
        