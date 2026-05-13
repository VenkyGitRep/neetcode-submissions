class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nineMap={}
        #Row check
        i=0
        j=0
        while(i<9):
            nineMap={}
            j=0
            while(j<9):
                cval=board[i][j]
                if(cval!="."):
                    val = ord(cval)-ord("1")+1
                    if(val>=1 and val<=9):
                        if(val in nineMap):
                            return False
                        else:
                            nineMap[val]=1
                j=j+1
            i=i+1
       
        #Column check
        i=0
        j=0
        while(i<9):
            nineMap={}
            j=0
            while(j<9):
                cval=board[j][i]
                if(cval!="."):
                    val = ord(cval)-ord("1")+1
                    if(val>=1 and val<=9):
                        if(val in nineMap):
                            return False
                        else:
                            nineMap[val]=1
                j=j+1
            i=i+1
        
        #Grid check
        i=0
        j=0

        while(i<9):
            j=0
            while(j<9):
                p=i
                q=j
                nineMap={}
                print(f"Grid starting {p},{q}")
                while(p<i+3):
                    q=j
                    while(q<j+3):
                        cval=board[p][q]
                        if(cval!="."):
                            val = ord(cval)-ord("1")+1
                            if(val>=1 and val<=9):
                                if(val in nineMap):
                                    return False
                                else:
                                    nineMap[val]=1
                        q=q+1
                    p=p+1
                j=j+3
            i=i+3




        return True