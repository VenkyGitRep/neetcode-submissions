class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        myDic={}
        for s in s1:
            if( s in myDic):
                myDic[s] = myDic[s] +1
            else:
                myDic[s]=1
        l=0
        r=0
        
        while(l<len(s2)):
            if(s2[l] in myDic):
                r=l
                myDick = dict(myDic)
                while(r-l<len(s1) and r<len(s2)):
                    if(s2[r] in myDick and myDick[s2[r]]>0):
                        myDick[s2[r]]=myDick[s2[r]]-1
                    else:
                        break
                    r=r+1
                found = True
                for ch in myDick:
                    if myDick[ch]!=0:
                        found = False
                if( found):
                    return True
            l=l+1
        return False
                            

