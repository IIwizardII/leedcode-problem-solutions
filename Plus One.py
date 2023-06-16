class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        listLen = len(digits)

        if digits[listLen-1] != 9:
            digits[listLen-1] = digits[listLen-1]+1
            return digits 
        elif digits[listLen-1] == 9 and listLen == 1:
            return [1, 0]
        elif digits[listLen-1] == 9:
            nineIndex = -1
            c = 0
            for i in range(listLen-1):
                if digits[listLen-2-i] == 9:
                    nineIndex = listLen-2-i
                    c = c+1
                elif digits[listLen-2-i] != 9:
                    break
            if nineIndex == 0:
                digits[nineIndex] = 1
                for i in range(nineIndex+1, listLen):
                    digits[i] = 0
                digits.append(0)
            elif nineIndex != 0 and nineIndex == -1:
                digits[listLen-2] = digits[listLen-2]+1
                for i in range(listLen-1, listLen):
                    digits[i] = 0
            elif nineIndex != 0 and nineIndex != -1:
                digits[nineIndex-1] = digits[nineIndex-1]+1
                for i in range(nineIndex, listLen):
                    digits[i] = 0
            return digits


