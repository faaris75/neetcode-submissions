class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen = {')':'(','}':'{',']':'['}
        for w in s:
            if w in closeToOpen:
                if stack and stack[-1] == closeToOpen[w]:
                    stack.pop()
                else:
                    return False            # I forgot the return false here
            else:
                stack.append(w)         # The indentation here was wrong too
        return True if not stack else False
                    
                
        
    