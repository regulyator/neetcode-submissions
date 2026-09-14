class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictMap = {}
        for char in s:
            if char not in dictMap:
                dictMap[char] = 0
            dictMap[char] = dictMap[char] + 1
        
        for char in t:
            if char not in dictMap:
                return False
            dictMap[char] = dictMap[char] - 1
        
        valueSet = set(dictMap.values())

        if len(valueSet) != 1 or 0 not in valueSet:
            return False
        
        return True
    
    