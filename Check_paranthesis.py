class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        stack = []
        mapping = {')':'(','}':'{',']':'['}
        
        for char in x:
            if char in '({[':
                 stack.append(char)
            elif  char in ')}]':
                if not stack:
                    return False
                if stack[-1] == mapping[char]:
                    stack.pop()
            else:
                return False
                    
        return not stack

