class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            return nums.index(target)
        else:
            numberOfItems = len(nums)
            if target>nums[numberOfItems-1]:
                return nums.index(nums[numberOfItems-1])+1
            elif target<nums[0]:
                return 0
            else:
                for i in range(numberOfItems):
                    if target>nums[i] and (i+1)<numberOfItems and target<nums[i+1]:
                        return nums.index(nums[i])+1
                    
