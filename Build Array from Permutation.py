class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        lenNum = len(nums)
        ansList = []
        
        for i in range(lenNum):
            ansList.append(nums[nums[i]])
            
        return ansList
