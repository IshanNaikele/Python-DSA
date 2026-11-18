#approach 1 
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        unique=set()
        for ch in sentence:
            unique.add(ch)
        return len(unique)==26

# approach 2 
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        visited=[False]*26
        for ch in sentence :
            index=ord(ch)-ord('a')
            visited[index]=True

        for value in visited:
            if value==False :
                return False
        return True