class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'{':'}','(':')','[':']'}
        stack= []

        for bracket in s:
            if bracket in mapping:
                stack.append(bracket)

            else:
                if not stack:
                    return False
                
                top_element = stack[-1]
                if bracket == mapping[top_element]:
                    stack.pop()
                else :
                    return False
        
        return not stack
        
        

                

            

        