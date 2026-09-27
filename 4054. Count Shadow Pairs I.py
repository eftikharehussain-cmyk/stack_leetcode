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