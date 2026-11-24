class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for each string: im gonna make a key that is just the letters, and will make it like if strs in key
        strr = defaultdict(list)
        for x in strs:
            count=[0]*26
            for i in x:
                count[ord(i)-ord('a')] += 1
            strr[tuple(count)].append(x)
        return list(strr.values())
        