class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans.append(nums)
        ans.append(nums)
        
        ansList = list(chain.from_iterable(ans))
        
        return ansList
