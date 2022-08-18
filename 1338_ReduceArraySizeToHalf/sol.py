class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dictA = Counter(arr)
        size = len(arr)
        count = 0
        res = 0
        
        values =sorted(dictA.values(), reverse = True)
        
        for val in values:
            count += val
            res +=1
            if not count * 2 < size:
                return res
                
            
        
        
        
