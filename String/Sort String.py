class Solution:
    def sortString(self, s: str) -> str:
        alpha=[0]*26
        for ch in s:
            ind=ord(ch)-ord('a')
            alpha[ind]+=1
            
        ans=""
        for i in range(26):
            ans+=chr(i+ord('a'))*alpha[i]
        
        return ans
         