# Two Sum - https://leetcode.com/problems/two-sum/
# Approach: Use a hashmap to store seen numbers and check for complement.
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashMap = {}

        for i, num in enumerate(numbers):
            diff = target - numbers[i]
            if(diff in hashMap):
                return(i, hashMap[diff])
            hashMap[num] = i
        return

# Example:
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))  # Output: [0, 1]
