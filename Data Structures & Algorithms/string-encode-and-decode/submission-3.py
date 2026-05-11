class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString=""
        for s in strs:
            for c in s:
                encodedString=encodedString+f"{ord(c):03d}"
            encodedString=encodedString+"-"
        #print(f"EncodedString:{encodedString}")
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStrings=[]
        #print(f"Decode string : {s}")
        n = len(s)
        i=0
        while i < n:
            w=""
            
            while(i+2<len(s) and s[i]!="-"):                
                #print(f"Decoding {s[i:i+3]}")
                c = chr(int(s[i:i+3]))
                #print(f"Decoded {s[i:i+3]} to {c}")
                w=w+c
                i=i+3
            #print(f"Deocded:{w}")
            decodedStrings.append(w)
            i=i+1

        return decodedStrings

