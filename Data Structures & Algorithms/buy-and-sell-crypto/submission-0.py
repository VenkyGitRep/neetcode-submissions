class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        minList=[prices[0]]*n
        maxList=[prices[-1]]*n

        i=1
        while(i<n):
            minList[i]=min(prices[i],minList[i-1])
            i=i+1
        
        i=n-2
        while(i>=0):
            maxList[i]=max(prices[i],maxList[i+1])
            i=i-1
        
        maxProfit = maxList[0]-minList[0]
        for i in range(n):
            maxProfit = max(maxProfit,maxList[i]-minList[i])
        return maxProfit

        