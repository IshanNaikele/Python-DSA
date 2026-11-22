class Solution:
    def isVowel(self,ch) :
        ch=ch.lower()
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
            return True
        return False
     
    def sortVowels(self, s: str) -> str:
        smallAlpha=[0]*26
        bigAlpha=[0]*26 
        for ch in s :
            if self.isVowel(ch) :
                if ch>='A' and ch<='Z' :
                    bigAlpha[ord(ch)-ord('A')]+=1
                else     :
                    smallAlpha[ord(ch)-ord('a')]+=1
        
        vowel=list()
        for i in range(0,26):
            while bigAlpha[i]>0 :
                vowel.append(chr(ord('A')+i))
                bigAlpha[i]-=1
        
        for i in range(0,26) :
            while smallAlpha[i]>0 :
                vowel.append(chr(ord('a')+i))
                smallAlpha[i]-=1
          
        index=0
        ans=list()
        for i in range(len(s)):
            if self.isVowel(s[i]) : 
                ans.append(vowel[index])
                index+=1 
            else :
                ans.append(s[i]) 
        
        return ''.join(ans)
        