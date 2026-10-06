class Solution:
    def calculate(self, s: str) -> int:
        st = s.replace(" ","")
        s = s.replace(" ","")
        first = []
        num = ""
        for i in s:
            if i.isdigit():
                num += i
            else:
                if num:
                    first.append(num)
                    num = ""
                first.append(i)
        if num:
            first.append(num)
        
            
        z_t = []
        symbols = {'+','-','/','*'}
        for i in first:
            if len(z_t) == 0:
                z_t.append(i)
            else:
                if z_t[-1] == '*':
                    z_t.pop()
                    b = z_t.pop()
                    z_t.append(int(b) * int(i))
                elif z_t[-1] == '/':
                    z_t.pop()
                    b = z_t.pop()
                    z_t.append(int(b) // int(i))
                elif i not in symbols and z_t[-1] not in symbols:
                    a = z_t.pop()
                    z_t.append(a + i)
                else:
                    z_t.append(i)
                    
        stack = []
        for j in z_t:
            if len(stack) == 0:
                stack.append(j)
            else:
                if stack[-1] == '-':
                    stack.pop()
                    a = stack.pop()
                    stack.append(int(a) - int(j))
                elif stack[-1] == '+':
                    stack.pop()
                    a = stack.pop()
                    stack.append(int(a) + int(j))
                else:
                    stack.append(j)
        return int(stack[-1])