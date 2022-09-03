class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        nums = range(10)
        
        for i in range(n-1):
            nums = {x*10+y for x in nums for y in [x%10+k, x%10-k] if x and 0<=y<10}
        return list(nums)    
                
            
