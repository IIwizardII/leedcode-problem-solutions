class Solution:
    def romanToInt(self, s: str) -> int:
        M = 1000
        D = 500
        C = 100 
        L = 50
        X = 10
        V = 5
        I = 1
        
        IV = 4
        IX = 9
        XL = 40
        XC = 90
        CD = 400
        CM = 900
        
        len_s = len(s)
        sum = 0
        star_point = 0
        flag = False
        for i in range(star_point, len_s):
            if flag == True:
                flag = False
                continue
            if i+1 != len_s:
                if s[i] == 'I' and s[i+1] == 'V':
                    sum = sum+IV
                    flag = True
                    continue
                elif s[i] == 'I' and s[i+1] == 'X':
                    sum = sum+IX
                    flag = True
                    continue
                elif s[i] == 'X' and s[i+1] == 'L':
                    sum = sum+XL
                    flag = True
                    continue
                elif s[i] == 'X' and s[i+1] == 'C':
                    sum = sum+XC
                    flag = True
                    continue
                elif s[i] == 'C' and s[i+1] == 'D':
                    sum = sum+CD
                    flag = True
                    continue
                elif s[i] == 'C' and s[i+1] == 'M':
                    sum = sum+CM
                    flag = True
                    continue
                    
            if s[i] == 'M':
                sum = sum+M
            elif s[i] == 'D':
                sum = sum+D
            elif s[i] == 'C':
                sum = sum+C
            elif s[i] == 'L':
                sum = sum+L
            elif s[i] == 'X':
                sum = sum+X
            elif s[i] == 'V':
                sum = sum+V
            elif s[i] == 'I':
                sum = sum+I
        
        return sum
