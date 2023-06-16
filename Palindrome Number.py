class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        lenNum = len(num)
        
        for i in range(lenNum):
            if num[i] != num[lenNum-i-1]:
                return False
            if(i > lenNum/2):
                break
        return True
