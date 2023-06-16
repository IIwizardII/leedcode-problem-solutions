class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        sLen = len(s)
        lastSpaceIndex = s.find(' ', 0)
        if lastSpaceIndex == -1:
            return sLen
        words = s.split()
        wordsCount = len(words)
        return len(words[wordsCount-1])
