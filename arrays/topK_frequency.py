class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) +1
        for n,c in count.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

        
        #this answer was right but it was in O(nlogn) time
        # hashMap = {}
        # for n in nums:
        #     hashMap[n] = hashMap.get(n, 0)+1
        # sorted_hash = sorted(hashMap, key=hashMap.get)
        # return  sorted_hash

solution = Solution()
print(solution.topKFrequent([1,1,1,1,2,2,2,2,2,3,3,3,3,3,3], 2))  # Output: [3, 2]