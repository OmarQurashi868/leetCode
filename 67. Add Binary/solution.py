class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = ""
        if len(a) >= len(b):
            big = a
            small = b
            length = len(a)
        else:
            big = b
            small = a
            length = len(b)
            
        diff = abs(len(a) - len(b))
        carry = False
        for i in range(length - 1, -1, -1):
            if i - diff < 0 :
                if carry:
                    if big[i] == "0":
                        sum = "1" + sum
                        carry = False
                        continue
                    else:
                        sum = "0" + sum
                        continue
                else:
                    sum = big[i] + sum
                    continue
            if not carry:
                if big[i] != small[i - diff]:
                    sum = "1" + sum
                    continue
                elif big[i] == "1" or small[i - diff] == "1":
                    sum = "0" + sum
                    carry = True
                    continue
                else:
                    sum = "0" + sum
                    continue
            if carry:
                if big[i] != small[i - diff]:
                    sum = "0" + sum
                    carry = True
                    continue
                elif big[i] == "1" or small[i - diff] == "1":
                    sum = "1" + sum
                    carry = True
                    continue
                else:
                    sum = "1" + sum
                    carry = False
                    continue
                    
        if carry:
            sum = "1" + sum
        return sum