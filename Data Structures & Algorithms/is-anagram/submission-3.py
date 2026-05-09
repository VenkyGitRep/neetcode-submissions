class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDict = [0]*26
        offset = ord('a')
        for c in s:
            charDict[ord(c)-offset]=charDict[ord(c)-offset]+1
        
        for c in t:
            if charDict[ord(c)-offset]==0:
                return False
            else:
                charDict[ord(c)-offset]=charDict[ord(c)-offset]-1
        for i in charDict:
            if(i!=0):
                return False
        return True
        