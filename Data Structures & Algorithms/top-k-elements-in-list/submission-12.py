class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for v in nums:
            freqMap[v] = 1 + freqMap.get(v, 0)
        bucket = {}
        maxV = 0
        for key, val in freqMap.items():
            if val > maxV:
                maxV = val
            if val not in bucket:
                bucket[val] = []
            bucket[val].append(key)
        result = []
        for n in range(maxV, 0, -1):
            if len(result) == k:
                return result
            if n in bucket:
                for elem in bucket[n]:
                    if len(result) == k:
                        return result
                    result.append(elem)
        return result
        