class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        MOD = 10**9 + 7
        dp = {}
        
        for num in arr:
            dp[num] = 1
        
        for i, num in enumerate(arr):
            for j in range(i):
                if not(num%arr[j]) and num//arr[j] in dp:
                    dp[num] += dp[arr[j]] * dp[num//arr[j]]
                    dp[num] %= MOD
                    
        return sum(dp.values()) % MOD             
                
        
        
        
        
        
