class Solution:
    def isClosing(self, c: chr) -> bool:
        if c is ")" or c is "}" or c is "]":
            return True
        else:
            return False
        
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0, len(s)):
            if not self.isClosing(s[i]):
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    current = ord(s[i])
                    last = ord(stack[len(stack) - 1])
                    diff = current - last
                    if diff > 0 and diff < 3:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) > 0:
            return False
        return True