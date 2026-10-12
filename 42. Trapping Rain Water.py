class Solution:
    def trap(self, hight: list[int]) -> int:
        left_wall = right_wall = 0
        n = len(hight)
        max_left = [0] * n
        max_right = [0] * n
        for i in range(n):
            j = -i-1
            max_left[i] = left_wall
            max_right[j] = right_wall
            left_wall = max(left_wall, hight[i])
            right_wall = max(right_wall, hight[j])
        ans = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            ans += max(0, pot - hight[i])
        return ans