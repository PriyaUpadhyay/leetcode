class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        dictN = Counter([int(i) for i in str(n)])
        
        num , i = 0,0
        while num <= 10**9:
            num = 2**i
            dictNum = Counter([int(i) for i in str(num)])
            if dictN == dictNum:
                return True
            i +=1
        return False     
        
