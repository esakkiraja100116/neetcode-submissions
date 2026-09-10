class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        source = set()
        for i in nums:
            if i in source:
                return True
            source.add(i)

        return False 

        
        