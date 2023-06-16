class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        
        length = len(nums1)
        
        if length%2 != 0:
            index = int((((length-1)/2)+1)-1)
            return float(nums1[index])
        else:
            index1 = int((length/2)-1)
            index2 = int(((length/2)-1)+1)
            return float((nums1[index1]+nums1[index2])/2)

