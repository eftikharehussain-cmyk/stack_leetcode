class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
    
        for i in s:
            if len(stack) < len(part):
                stack.append(i)
                if len(stack) == len(part) and "".join(stack) == part:
                    stack = []
            else:
                stack.append(i)
                if "".join(stack[len(stack) - len(part) :]) == part:
                    stack = stack[:len(stack) - len(part)]
                # stack.append(i)
        if "".join(stack) == part:
            return ""
        return ("".join(stack))