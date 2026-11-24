# Approach 1 :
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

# Approach 2 :
class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)
        i=0
        s=s[::-1]
        ans=list()
        while i<n :
            temp=list()
            while i<n and s[i]==' ':
                i+=1

            if i >=n :
                break
            
            while i<n and s[i]!=' ':
                temp.append(s[i])
                i+=1
            
            temp.reverse()
            ans.append(''.join(temp)) 
            ans.append(' ')
        
        ans.pop()
        return ''.join(ans)
        