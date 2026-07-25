class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} #track amount of times each number is seen 
        freq = [[] for i in range(len(nums) + 1)] #checking amount of times the number occurs with bins for each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) -1, 0, -1 ):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


                





        