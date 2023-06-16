class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0 or k == len(nums): nums
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
