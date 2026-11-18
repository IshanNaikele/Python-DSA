#approach 1 :
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for ch in address:
            if ch==".":
                ans+=f"[{ch}]"
            else :
                ans+=ch
        return ans

# approach 2 
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=list()
        for ch in address:
            if ch==".":
                ans.append(f"[{ch}]")
            else :
                ans.append(ch)
        return ''.join(ans)
        