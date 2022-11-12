class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        length = len(str(x))
        if length % 2 == 0:
            limit = length / 2
        else:
            limit = (length - 1) / 2

        
        for i in range(int(limit)):
            if string[i] != string[length - i - 1]:
                return False
        
        return True