
class Solution:
    def isValid(self, s: str) -> bool:
        
        t1 = '('
        t11 = ')'
        t2 = '['
        t22 = ']'
        t3 = '{'
        t33 = '}'

        stack = []

        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if s[i] == t11 and stack[-1] == t1:
                    stack.pop(-1)
                elif s[i] == t22 and stack[-1] == t2:
                    stack.pop(-1)
                elif s[i] == t33 and stack[-1] == t3:
                    stack.pop(-1)
                else:
                    stack.append(s[i])
        ok = True
        if len(stack) > 0:
            ok = False
        return ok