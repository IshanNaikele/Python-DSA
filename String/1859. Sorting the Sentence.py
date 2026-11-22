#Approach 1 
class Solution:
    def sortSentence(self, s: str) -> str:
        s+=" "
        temp=list()
        store=[""]*10
        for ch in s :
            if ch==' ' :
                index=ord(temp[-1])-ord('0')
                temp.pop()
                store[index]=''.join(temp)
                temp.clear()
            else :
                temp.append(ch)
        
        ans=""
        for i in range(1,10):
            if store[i]=="" :
                break
            ans+=store[i]+" "
        
        ans=ans[:-1]
        return ans        

# Approach 2 
class Solution:
    def sortSentence(self, s: str) -> str:
        store=[""]*10 
        for word in s.split():
            index=ord(word[-1])-ord('0')
            store[index]=word[:-1]
        return ' '.join(store[1:]).strip()