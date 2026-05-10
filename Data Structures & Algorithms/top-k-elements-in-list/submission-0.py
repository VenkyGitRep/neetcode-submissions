import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for n in nums:
            freqDict[n] = freqDict.get(n,0)+1
        
        minHeap = []
        for entry,freq in freqDict.items():           
            heapq.heappush(minHeap,(-freq,entry))
        output = []
        

        while(k>0):
            freq,entry = heapq.heappop(minHeap)
            
            output.append(entry)
            k=k-1
        return output
        
