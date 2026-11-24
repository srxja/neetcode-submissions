class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # //my approach: for each number: the other = target - that number, and hash table: find if its there
        index = {}
        for i,x in enumerate(nums):
            if target-x not in index:
                index[x] = []
                index[x].append(i)
            elif target-x in index:
                return [index[target-x][0],i]



                
            