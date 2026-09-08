class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        source = dict()
        dest = dict()

        for i in s:
            source[i] = source.get(i, 0) + 1
        
        for j in t:
            dest[j] = dest.get(j, 0) + 1    

        for key, value in source.items():
            
            if key in dest and dest[key] == value:
                pass
            else:
                return False
        
        return True