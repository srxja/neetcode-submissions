class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for i in nums:
            freq[i]+=1
        freq = dict(sorted(freq.items(),key = lambda item:item[1], reverse = True))
        return list(islice(freq.keys(), k))

