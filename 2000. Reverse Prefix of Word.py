class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        target = 0
        ok = True
        for i in range(len(word)):
            if word[i] == ch:
                ok = False
                stack.append(word[i])
                target = i + 1
                break
            else:
                stack.append(word[i])
        
        stack = stack[::-1]
        if ok:
            return word
        return ("".join(stack) + word[target:])