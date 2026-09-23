class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
    
        for i in s:
            if len(stack) < k-1:
                stack.append(i)
            else:
                if i == stack[-1]:
                    t = stack[len(stack) - (k-1):]
                
                    if len(set(t)) == 1:
                        stack = stack[:len(stack) - (k-1)]
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        return "".join(stack)