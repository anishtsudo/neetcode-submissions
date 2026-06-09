class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in value:
                return [value[diff], i]
            value[n] = i
        