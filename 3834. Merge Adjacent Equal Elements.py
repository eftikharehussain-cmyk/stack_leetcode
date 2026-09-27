class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for i in nums:
            if len(stack) == 0:
                stack.append(i)
            else:
                if stack[-1] == i:
                    stack[-1] = stack[-1] + i
                    while len(stack) >= 2 and stack[-1] == stack[-2]:
                        stack[-2] = stack[-1] + stack[-1]
                        stack.pop()
                else:
                    stack.append(i)
        return stack