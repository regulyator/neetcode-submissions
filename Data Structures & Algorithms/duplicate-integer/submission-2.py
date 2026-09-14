class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for el in nums:
            numsSet.add(el)
        if len(nums) != len(numsSet):
            return True
        return False