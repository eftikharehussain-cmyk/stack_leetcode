class Solution:
    def removeKdigits(self, num: str, t: int) -> str:
        if len(num) <= t:
            return '0'
        else:
            stack = []
            for i in num:
                while stack and t > 0 and stack[-1] > i:
                    stack.pop()
                    t -= 1
                stack.append(i)
            if t:
                stack = stack[:-t]
            result = "".join(stack).lstrip('0')
            return result if result else "0"





