class Solution:
    def rotateClockwise(self,s1,s2):
        n=len(s1)
        for i in range(n):
            if s1[i]!=s2[(i+2)%n] :
                return False
        return True
    
    def rotateAntiClockwise(self,s1,s2):
        n=len(s1)
        for i in range(n-1,-1,-1):
            if s1[i]!=s2[(n+i-2)%n] :
                return False
        return True
        
    def isRotated(self,s1,s2):
        if len(s1)!=len(s2) :
            return False
        return self.rotateClockwise(s1,s2) or self.rotateAntiClockwise(s1,s2)
        
        