class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        cnt = 0
        _chr = ""
        for i in range(len(s)-1, -1, -1):
            if s[i].isalpha():
                _chr += s[i]
            else:
                break
        return len(_chr)
