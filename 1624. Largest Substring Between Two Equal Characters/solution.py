class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hashmap = {}
        out = -1
        for i in range (0, len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = i
            else:
                if i - hashmap[s[i]] - 1 > out:
                    out = i - hashmap[s[i]] - 1
        return out