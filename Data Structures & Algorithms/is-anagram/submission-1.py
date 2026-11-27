class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # freq = defaultdict(list)
        # for x
        s = sorted(s)
        t = sorted(t)
        return s==t