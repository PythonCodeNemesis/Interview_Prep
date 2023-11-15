import sys
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)
        def f(i, max_reach):
            if i==n:
                return 0
            if i>n:
                return sys.maxsize
            ans = sys.maxsize
            
            if days[i]>=max_reach:
                tick_1=costs[0]+f(i+1,days[i]+1)
                tick_2=costs[1]+f(i+1,days[i]+7)
                tick_3=costs[2]+f(i+1,days[i]+30)
                ans = min(ans,tick_1,tick_2,tick_3)
                return ans
            else:
                not_buy=f(i+1,max_reach)
                ans = min(ans, not_buy)
                return ans
    
        return f(0,0)
