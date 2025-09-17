# make a function that can show the frequency of a list of nums

class Solution(object):
    def frequency(self, nums: list[int]):
        hashMap = {}
        for n in nums:
            hashMap[n] = hashMap.get(n, 0)+1
        return hashMap

# Example:
solution = Solution()
print(solution.frequency([1,2,1,3,1,2,1,2,2,3,1,4]))  # Output: {1: 5, 2: 4, 3: 2, 4: 1}