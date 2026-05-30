class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i,v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            left=i+1
            right = len(nums)-1
            while(left<right):
                if(nums[left]+nums[right]+v==0):
                    output.append([v,nums[left],nums[right]])
                    while(left<right and nums[left]==nums[left+1]):
                        left=left+1
                    while(right>left and nums[right]==nums[right-1]):
                        right=right-1
                    left += 1
                    right -= 1
                elif(nums[left]+nums[right]+v<0):
                    left=left+1
                else:
                    right=right-1
                    
        return output