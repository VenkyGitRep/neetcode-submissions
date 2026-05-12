class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd=[1]*len(nums)
        rightProd=[1]*len(nums)
        output=[1]*len(nums)

        leftProd[0]=nums[0]
        i=1        
        while i<len(nums):
            leftProd[i]=leftProd[i-1]*nums[i]
            i=i+1
        
        rightProd[len(nums)-1]=nums[-1]
        i=len(nums)-2
        while(i>=0):
            rightProd[i]=rightProd[i+1]*nums[i]
            i=i-1
        
        output[0]=rightProd[1]
        output[len(nums)-1]=leftProd[-2]
        i=1
        while(i<len(nums)-1):
            output[i]=leftProd[i-1]*rightProd[i+1]
            i=i+1
        return output