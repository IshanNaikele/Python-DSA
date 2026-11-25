class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq=dict()
        left=right=minLen=0
        n=len(s)

        while right<n :
            freq[s[right]]=freq.get(s[right],0)+1
            while left<=right and freq[s[right]]>1 :
                freq[s[left]]-=1
                left+=1
            minLen=max(minLen,right-left+1)
            right+=1
        return minLen