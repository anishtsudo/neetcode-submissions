class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,t in enumerate(nums):
            need = target - t
            if need in seen:
                return[seen[need], i]

            seen[t] = i
            
              

            
        