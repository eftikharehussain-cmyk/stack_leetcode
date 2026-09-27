# first mode
class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        

        
        i = len(nums)-1
        cnt = 0
        while i >= 0:
            
            _max = nums[i]
            _min = nums[i]
            for j in range(i,-1,-1):
                if nums[j] < _max and nums[j] <= _min:
                    _min = nums[j]
                    cnt += 1
            i -= 1
        return cnt
    
# second mode
from bisect import bisect_left
class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        ans = 0
        s = []
        
        for i in nums:
            while s and s[-1] > i:
                s.pop()
            ans += bisect_left(s, i)
            s.append(i)
        return ans
nums = [3, 1, 4, 1, 5]

sol = Solution()

print(sol.shadowPairs(nums))