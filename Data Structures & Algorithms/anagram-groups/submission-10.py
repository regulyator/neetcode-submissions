class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultMap = {}
        for s in strs:
            sList = list(range(26))
            for char in s:
                cIdx = ord(char) - 97
                sList[cIdx] = sList[cIdx] + 1
            sTuple = tuple(sList)    
            if sTuple not in resultMap:
                resultMap[sTuple] = []
            resultMap[sTuple].append(s)
        return list(resultMap.values())
        
        