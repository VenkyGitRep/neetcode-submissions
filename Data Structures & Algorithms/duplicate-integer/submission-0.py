class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countDict = {}
        for n in nums:
            if(n in countDict):
                return True
            countDict[n]=1
        return False