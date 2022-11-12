class Solution:
    def add(self, digits, i) -> List[int]:
        if digits[i] < 9:
            digits[i] += 1
            return digits
        elif i == 0:
            digits[i] = 0
            digits.insert(0, 1)
            return digits
        else:
            digits[i] = 0
            return self.add(digits, i-1)
        
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.add(digits, len(digits) - 1)