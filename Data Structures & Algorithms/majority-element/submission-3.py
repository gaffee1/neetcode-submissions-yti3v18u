class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dico = {}
        for e in nums:
            if e in dico:
                dico[e] += 1
            else:
                dico.update({e : 1})

        max = int()
        key = int()
        for key, val in dico.items():
            if val > (len(nums) / 2):
                return key