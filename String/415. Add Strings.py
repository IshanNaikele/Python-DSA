class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1=num1[::-1]
        num2=num2[::-1]
        index1=index2=summ=0
        m=len(num1)
        n=len(num2)
        ans=list()
        while index1<m or index2<n or summ :
            if index1<m :
                summ+=ord(num1[index1])-ord('0')
                index1+=1
            if index2<n :
                summ+=ord(num2[index2])-ord('0')
                index2+=1
            carry=summ//10
            summ=summ%10
            ans.append(summ)
            summ=carry
        
        ans=ans[::-1]
        return ''.join(map(str,ans))