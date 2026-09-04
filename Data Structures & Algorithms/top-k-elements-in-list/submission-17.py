class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsdict = {}
        for num in nums:
            numsdict[num] = numsdict.get(num, 0) + 1
        
        numfreqs = []
        for unique_num in list(set(nums)):
            numfreqs.append([numsdict[unique_num], unique_num])
        numfreqs.sort()

        output = []
        for i in range(len(numfreqs) - k, len(numfreqs)):
            output.append(numfreqs[i][1])

        return output
        
        