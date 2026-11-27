class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 27
        countt = [0] * 27
        for x in s:
            print(ord(x) - ord('a'))
            counts[ord(x) - ord('a')] +=1
        for x in t:
            countt[ord(x) - ord('a')] +=1
        return counts == countt