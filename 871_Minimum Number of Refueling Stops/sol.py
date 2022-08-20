class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if(target == startFuel or target<startFuel) :
            return 0
        
        maxReach  = startFuel
        pq = []
        count = 0
        index =  0
        
        while(maxReach < target):
            while(index<len(stations) and stations[index][0]<=maxReach):
                pq.append(stations[index][1])
                index+=1
            if len(pq)==0:
                return -1
            pq = sorted(pq)
            maxReach += pq.pop()
            count+=1
        return count    
        
        
        
