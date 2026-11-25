class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for i in nums:
            freq[i]+=1
        major_freq = [[]for _ in range(len(nums)+1)]
        for i in freq:
            major_freq[freq[i]].append(i)
        ans = []
        n=k
        for i in range(len(nums),-1,-1):
            if k ==0:
                break
            if len(major_freq[i]) <= k:
                k -= len(major_freq[i])
                ans.extend(major_freq[i])
            elif len(major_freq[i]) > k:
                ans.extend(major_freq[i][:k])
                k = 0
        return ans
