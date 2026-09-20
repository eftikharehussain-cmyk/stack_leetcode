
class Solution:
    def reverse(self, x: int) -> int:
        _str = str(x)
        length = len(_str)
        _chr = ""
        _chr1 = ""
        ok = True
        tar = 0
        if _str[0] == '-':
            _chr += _str[0]
            for i in range(length-1, 0, -1):
                _chr += _str[i]
            if _chr[1] == '0':

                for j in range(1, length):
                    if _str[j] != '0':
                        tar = j
                        break
                result = int((_chr[0] + _chr[tar:]))
                

            else:
                result = int(_chr)
        else:
            for i in range(length-1,-1,-1):
                _chr += _str[i]
            
            if _chr[0] == '0':
                for j in range(1, length):
                    if _chr[j] != '0':
                        tar = j
                        break
            
            result = int(_chr[tar:])

        if result < -2147483648 or result > 2147483647:
            return 0
        return result