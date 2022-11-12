class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        for i in range(0, len(s)):
            if i + 1 < len(s):
                if table[s[i]] < table[s[i + 1]]:
                    number -= table[s[i]]
                else:
                    number += table[s[i]]
            else:
                number += table[s[i]]
        
        return number