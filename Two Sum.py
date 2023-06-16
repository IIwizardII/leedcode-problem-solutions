class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numLen = len(nums)
        indices = []
        for i in range(0, numLen):
            for j in range(i+1, numLen):
                if((nums[i]+nums[j]) == target):
                    indices.append(i)
                    indices.append(j)
                    break
        
        return indices
            
