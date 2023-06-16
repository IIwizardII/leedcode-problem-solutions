class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lenWord = len(word)
        
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper:
            flag = False
            for i in range(1, lenWord):
                if word[i].isupper():
                    return False
            return True
