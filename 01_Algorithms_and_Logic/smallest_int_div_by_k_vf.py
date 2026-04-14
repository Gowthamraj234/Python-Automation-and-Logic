class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n=1 
        for i in range(1,k+1):
            if n%k==0:
                return i
            n=10*(n%k)+1
        return -1