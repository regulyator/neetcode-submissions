class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictVal = {}
        for idx in range(len(nums)):
            if target - nums[idx] in dictVal:
                return [dictVal[target - nums[idx]], idx]
            dictVal[nums[idx]] = idx

        