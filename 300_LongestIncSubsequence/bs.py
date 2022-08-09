class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for num in nums[1:]:
            if sub[-1] < num:
                sub.append(num)
            else:
                i = 0
                while sub[i] < num:
                    i += 1
                sub[i] = num
        return len(sub)
        
