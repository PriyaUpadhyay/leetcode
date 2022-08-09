class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        counts = [1]*len(nums)
        for i in range(1,len(nums)):
            temp = [1]*1
            for j in range(0,i):
                if(nums[i]>nums[j]):
                    temp.append(counts[i] + counts[j])
            counts[i] = max(temp)
        return max(counts)    
                    
                    
                
            
        
        
