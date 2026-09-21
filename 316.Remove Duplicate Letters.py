
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        _dict = {}
        for i in s:
            if i not in _dict:
                _dict[i] = 1
            else:
                _dict[i] += 1
        
        stack = []
        _set = set()

        for i in s:
            _dict[i] -= 1
            if i in _set:
                continue
            while stack and stack[-1] > i and _dict[stack[-1]] > 0:
                _set.remove(stack.pop())
            stack.append(i)
            _set.add(i)
        return "".join(stack)