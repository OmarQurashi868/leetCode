class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        sLength = 200
        
        for str in strs:
            if len(str) == 0:
                return ""
            if sLength > len(str):
                sLength = len(str)
        
        for i in range(0, sLength):
            for j in range(0, len(strs)):
                if j + 1 < len(strs):
                    if strs[j][i] != strs[j + 1][i]:
                        return pre
            pre = pre + strs[0][i]
        return pre