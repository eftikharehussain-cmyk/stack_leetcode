
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        _dict = {}
        for i in range(len(nums2)):
            _dict[nums2[i]] = i
        
        answer = []

        for i in range(len(nums1)):
            ok = -1
            for j in range(_dict[nums1[i]], len(nums2)):
                if nums2[j] > nums1[i]:
                    ok = nums2[j]
                    break
            answer.append(ok)
        return answer