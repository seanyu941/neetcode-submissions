class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        kv = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in kv:
                if stack and kv[c] == stack[-1]: 
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)
        
        return True if not stack else False