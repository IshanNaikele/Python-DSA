class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            number=ord(num[i])-ord('0')
            if number%2==1 :
                return num[:i+1]
        return ""
        