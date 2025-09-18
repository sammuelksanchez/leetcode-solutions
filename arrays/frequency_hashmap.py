# make a function that can show the frequency of a list of nums
class Solution(object):
    def frequency(self, nums: list[int]):
        hashMap = {}
        for n in nums:
            hashMap[n] = hashMap.get(n, 0)+1
        return  hashMap

# Example:
solution = Solution()
print(solution.frequency([1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]))  # Output: {1: 4, 2: 5, 3: 6}
