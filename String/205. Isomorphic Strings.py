class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freq1=dict()
        freq2=dict()

        for i in range(len(s)):
            if s[i] in freq1 and freq1[s[i]]!=t[i]:
                return False
             
            if t[i] in freq2 and freq2[t[i]]!=s[i]: 
                return False 

            freq1[s[i]]=t[i]
            freq2[t[i]]=s[i]
        
        return True