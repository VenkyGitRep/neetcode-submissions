class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charDict = {}
        for c in s:
            if(c in charDict):
                charDict[c]=charDict[c]+1
            else:
                charDict[c]=1
        
        for c in t:
            if(c not in charDict):
                return False
            else:
                charDict[c] = charDict[c]-1
                if(charDict[c]==0):
                    del charDict[c]
        return True
