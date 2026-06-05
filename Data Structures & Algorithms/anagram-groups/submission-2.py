class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for s in strs:
            key = self.getKey(s)
            if key in anagramMap:
                anagramMap[key].append(s)
            else:
                anagramMap[key] = [s]
        return list(anagramMap.values())
        
    
    def getKey(self, s:str)->str:
        key = [0]*26
        for c in s:
            key[ord(c)-ord('a')]+=1
        return ",".join(map(str,key))





