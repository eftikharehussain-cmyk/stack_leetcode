class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        length = len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < length:
                length = len(strs[i])

        start = 0
        ok = True
        ans = ""
        _chr = []
        while start < length and ok:
            for i in strs:
                _chr.append(i[start])
            if len(set(_chr)) == 1:
                ans += _chr[0]
                _chr = []
            else:
                ok = False
            start += 1
        return ans