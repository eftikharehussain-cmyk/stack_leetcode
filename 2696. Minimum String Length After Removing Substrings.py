class Solution:
    def minLength(self, s: str) -> int:
        stack = []
    
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            else:
                if i == 'B' and stack[-1] == 'A':
                    stack.pop(-1)
                elif i == 'D' and stack[-1] == 'C':
                    stack.pop(-1)
                else:
                    stack.append(i)
        return len(stack)