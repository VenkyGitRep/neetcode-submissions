class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myDict = {}
        l=0
        r=0
        maxLength = 0
        while(r<len(s)):
            if s[r] in myDict:
                myDict[s[r]]+=1
            else:
                myDict[s[r]]=1
            
            maxFreq  = max(myDict.values())
            curLength = r-l+1
            if(curLength-maxFreq>k):
                #increase L untile size is ==k
                while(curLength-maxFreq>k):
                    if myDict[s[l]]>1:
                        myDict[s[l]]=myDict[s[l]]-1
                    elif myDict[s[l]]==1:
                        del myDict[s[l]]
                    else:
                        print("Aint no way Hosey")
                    l=l+1
                    maxFreq  = max(myDict.values())
                    curLength = r-l+1
            
            maxLength = max(maxLength,r-l+1)
            r=r+1
            
        return maxLength
            
                
                    
