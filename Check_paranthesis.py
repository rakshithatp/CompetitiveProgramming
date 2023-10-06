class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(x):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
    
        for char in x:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False
    
        return len(stack) == 0

