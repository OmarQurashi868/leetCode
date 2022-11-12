class Solution:
    def recurse(self,out: List[List[int]] ,rows: int) -> List[List[int]]:
        current = []
        if len(out) == rows:
            return out
        else:
            current.append(1)
            for i in range(1, len(out[len(out) - 1])):
                sum = out[len(out) - 1][i - 1] + out[len(out) - 1][i]
                current.append(sum)       
            current.append(1)
            out.append(current)
            return self.recurse(out, rows)
        
    def generate(self, numRows: int) -> List[List[int]]:
        return self.recurse([[1]], numRows)