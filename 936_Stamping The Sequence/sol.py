class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def canStamp(start):
            flag = False
            for i in range(lenS):
                if(targetList[start+i]=='?'):
                    continue
                flag = True
                
                if stamp[i] != targetList[start+i]:
                    return False
            return flag    
        
        
        
        lenS = len(stamp)
        lenT = len(target)
        
        # Converting to list bcz in python string is immutable
        targetList = list(target)
        
        # how many letters are not question marks
        remaining = lenT
        
        res = []
        
        while remaining:
            flag = False;
            
            for i in range(lenT - lenS+1):
                if canStamp(i):
                    flag = True
                    res.append(i)
                    for j in range(lenS):
                        if targetList[i+j] != '?':
                            targetList[i+j] = '?'
                            remaining -= 1
            # if didnt found any place for stamping than return empty list
            if not flag:
                return []
        
        #return reverse order of the res
        return res[::-1]     
            
        
