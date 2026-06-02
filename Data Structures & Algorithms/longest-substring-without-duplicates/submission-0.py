class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        maxLength=0
        uniqChars={}
        while(r<len(s)):
            if(s[r] not in uniqChars):
                uniqChars[s[r]]=r
                r=r+1
                maxLength = max(maxLength,r-l)
            else:
                l = uniqChars[s[r]]+1
                r = l
                uniqChars={}

        return maxLength
            