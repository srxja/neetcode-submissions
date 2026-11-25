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
            if len(major_freq[i])>0:
                k-=1
                ans.extend(major_freq[i])
                if k==0:
                    break
        return ans[:n]
