class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        s_p = []
        s_s = []
        
        for i in range(len(position)-1,-1,-1):
            if len(s_p) == 0:
                s_p.append(position[i])
                s_s.append(speed[i])
            else:
                if abs(s_p[-1] - position[i]) <= distance or s_s[-1] < speed[i]:
                    s_p.pop()
                    s_p.append(position[i])
                    continue
                else:
                    s_p.append(position[i])
                    s_s.append(speed[i])
        return (len(s_p))