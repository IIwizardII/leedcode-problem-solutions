class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary = {
            '1':'I',
            '5':'V',
            
            '6':'VI',
            '7':'VII',
            '8':'VIII',
            '3':'III',
            '2':'II',

            '10':'X',
            '50':'L',

            '60':'LX',
            '70':'LXX',
            '80':'LXXX',
            '30':'XXX',
            '20':'XX',

            '100':'C',
            '500':'D',

            '600':'DC',
            '700':'DCC',
            '800':'DCCC',
            '300':'CCC',
            '200':'CC',

            '1000':'M',
            '2000':'MM',
            '3000':'MMM',

            '4':'IV',
            '9':'IX',
            '40':'XL',
            '90':'XC',
            '400':'CD',
            '900':'CM'
        }
        result = ''
        numInString = str(num)
        if numInString in dictionary:
            return dictionary[numInString]
        
        flag = True
        divisor = 10
        remainder = None
        
        divident = num
        step = 1
        for i in reversed(range(0, len(numInString), step)):
            remainder = divident % divisor
            print(remainder)
            if remainder == 0:
                divisor = divisor * 10
                
                continue
            if str(remainder) in dictionary:
                result = dictionary[str(remainder)] + result
                divisor = divisor * 10
                divident = (divident - remainder)

        return result

