class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for each string: im gonna make a key that is just the letters, and will make it like if strs in key
        strr = {}
        for x in strs:
            x1 = "".join(sorted(x))
            if x1 not in strr:
                strr[x1] = []
            strr[x1].append(x)
        ans = []
        for x in strr:
            ans.append(strr[x])
        return ans
        