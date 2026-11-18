class Solution:
    def longestPalindrome(self, s: str) -> int:
        smallAlpha=[0]*26
        bigAlpha=[0]*26

        for ch in s:
            if ch>='A' and ch<='Z':
                bigAlpha[ord(ch)-ord('A')]+=1
            else :
                smallAlpha[ord(ch)-ord('a')]+=1
        
        ans=0;
        oddFound=False;
        for i in range(26):
            if smallAlpha[i]%2==0 :
                ans+=smallAlpha[i]
            else   :                
                ans+=smallAlpha[i]-1
                oddFound=True
            
            if bigAlpha[i]%2==0 :
                ans+=bigAlpha[i]
            else :                
                ans+=bigAlpha[i]-1
                oddFound=True
            
        
        if oddFound :
            ans+=1
        return ans