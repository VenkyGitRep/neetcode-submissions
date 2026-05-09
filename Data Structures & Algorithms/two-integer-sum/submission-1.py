class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            n=nums[i]
            partner = target-n
            if( partner in numDict):
                return [numDict[partner],i]
            else:
                numDict[n]=i
        return []