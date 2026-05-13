class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unums = set()
        for n in nums:
            unums.add(n)
        maxLength = 0
        for n in unums:
            l=0
            c=n
            if c-1 not in unums:
                while(c in unums):
                    l=l+1
                    c=c+1
            maxLength = max(maxLength,l)
        return maxLength

            