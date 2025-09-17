class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

    # even tho this is not allowed to be part of the answer cause it takes O(n) space
    # im still proud of it cause it gives right answer to the prefix and postfix arrays
    #   prefix = [0] * len(nums)
    #   postfix = [0] * len(nums)
    #   prefix[0] = nums[0]
    #   postfix[len(nums)-1] = nums[len(nums)-1]
    #   for i in range(1, len(nums)):
    #     prefix[i] = nums[i] * prefix[i-1]
    #     postfix[(len(nums)-1)-i] = nums[(len(nums)-1)-i] * postfix[len(nums)-i]
    #   print(prefix)
    #   print(postfix)
        


solution = Solution()
print(solution.productExceptSelf([1,2,4,6]))  # Output: [48, 24, 12, 8]