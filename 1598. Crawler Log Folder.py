class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = []
        for i in logs:
            if i != "./" and i != '../':
                stack.append(i)
            elif i == "../":
                if stack:
                    stack.pop()
            elif i == './':
                continue
        return len(stack)