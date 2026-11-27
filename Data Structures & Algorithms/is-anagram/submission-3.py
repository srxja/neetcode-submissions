class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26
        for x in s:
            counts[ord(x) - ord('a')] +=1
        for x in t:
            counts[ord(x) - ord('a')] -=1
        return all(x==0 for x in counts)