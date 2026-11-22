class Solution:
    def caseSort(self,s):
        smallAlpha=[0]*26
        bigAlpha=[0]*26 
        for ch in s :
            if ch>='A' and ch<='Z' :
                bigAlpha[ord(ch)-ord('A')]+=1
            else   :
                smallAlpha[ord(ch)-ord('a')]+=1
        
        big=""
        small=""
        for i in range(26):
            while bigAlpha[i]>0 :
                big+=(chr(ord('A')+i))
                bigAlpha[i]-=1;
            
            while smallAlpha[i]>0 :
                small+=(chr(ord('a')+i))
                smallAlpha[i]-=1
            
        index1=index2=0
        ans=list()
        for i in range(len(s)):
            ch=s[i]
            if ch>='A' and ch<='Z' :
                ans.append(big[index1])
                index1+=1
            else     :
                ans.append(small[index2])
                index2+=1
        
        return ''.join(ans)