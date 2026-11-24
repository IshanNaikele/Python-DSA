#Approach 1 :
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=list()
        openBracket=0
        for ch in s :
            if ch=='(' :
                openBracket+=1
                if openBracket>1 :
                    ans.append(ch)
            else :
                if openBracket>1 :
                    ans.append(ch)
                openBracket-=1
            
        return ''.join(ans)


        