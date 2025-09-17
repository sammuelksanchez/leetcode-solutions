class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        if countS == countT:
            print(countS, countT)
            return True
        else:
            return False




# Example:
solution = Solution()
print(solution.isAnagram("xx", "x"))  # Output: [0, 1]