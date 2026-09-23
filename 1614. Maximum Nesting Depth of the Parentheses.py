class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = []
        
        _max = 0
        
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                _max = max(_max, len(stack))
                stack.pop(-1)
        return _max