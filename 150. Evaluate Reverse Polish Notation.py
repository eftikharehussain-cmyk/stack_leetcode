class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        a = {'/', '-', '+', '*'}
        stack = []
        
        for i in tokens:
            if i not in a:
                stack.append(int(i))
            else:
                b = stack.pop()
                c = stack.pop()
                if i == '+':
                    stack.append(c + b)
                elif i == '-':
                    stack.append(c - b)
                elif i == '*':
                    stack.append(c * b)
                else:
                    stack.append(int(c / b))
        return (stack[-1])