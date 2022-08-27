class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictM = Counter(magazine)
        dictR = Counter(ransomNote)
        
        for k in dictR:
            if dictR[k]>dictM.get(k,-1):
                return False
        return True    
                
        
