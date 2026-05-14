class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while(l<=r):
            left = s[l]
            right = s[r]
            
            while not(
                (left>='a' and left<='z') 
                or (left>='A' and left<='Z') 
                or (left>='0' and left<='9')):
                l=l+1
                if(l<len(s)):
                    left = s[l]
                else:
                    break
                
            while not(
                (right>='a' and right<='z') 
                or (right>='A' and right<='Z') 
                or (right>='0' and right<='9')):
                r=r-1
                if(r>=0):
                    right = s[r]
                else:
                    break
            print(f"left:{left}, right:{right}")
            
            if(l<=r and left.lower()!=right.lower()):
                return False
            l=l+1
            r=r-1


        return True