#User function Template for python3
import collections
class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        #insert all in stack
        # pop top 2 from stack
        # each pair of i and j, check if i knows j and j knows i
        # if i knows j, i cannot be celebrity
        # you shall be left with 1
        # in the end check if this left over candidate knows anyone or not
        
        stack = collections.deque()
        for i in range(n):
            stack.append(i)
            
        while len(stack)>=2:
            cand1 = stack.pop()
            cand2 = stack.pop()
            if M[cand1][cand2]==1:
                stack.append(cand2)
            elif M[cand2][cand1]==1:
                stack.append(cand1)
            
        cand = stack.pop()
        for i in range(n):
            if i != cand and (M[cand][i] == 1 or M[i][cand] == 0):
                return -1
        return cand



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends
