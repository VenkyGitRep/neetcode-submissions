class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for i in range(len(strs)):
            key = self.getKey(strs[i])
            if key in anagramMap:
                anagramMap.get(key,[]).append(strs[i])
            else:
                anagramMap[key]=[strs[i]]
           
        return list(anagramMap.values())

    def getKey(self,s:str)->str:
        charDict = [0]*26
        offset = ord('a')
        for c in s:
            charDict[ord(c)-offset]=charDict[ord(c)-offset]+1
        key =""
        for i in charDict:
            key = key+str(i)+"-"
        print(f"Word:{s},Key:{key}")

        return key

        