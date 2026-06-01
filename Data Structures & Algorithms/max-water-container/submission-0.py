class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxvol = (right-left) * min(heights[left],heights[right])
        while(left<right):
            if(heights[left]<heights[right]):
                left= left+1
            else:
                right = right-1
            maxvol = max(maxvol,(right-left) * min(heights[left],heights[right]))
        return maxvol
            

