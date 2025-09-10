class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        False

# Example:
solution = Solution()
print(solution.hasDuplicate([1,2,3,3]))  # Output: True