class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            difference = target - nums[i]
            for j in range(len(nums)):
                if i != j:
                    if difference == nums[j]:
                        return [i, j]