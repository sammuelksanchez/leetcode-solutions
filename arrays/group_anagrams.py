class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}

        for word in strs:
            counts = [0]*26
            for ch in word:
                counts[ord(ch) - ord('a')] += 1
            key = tuple(counts)

            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)

        # We only need the grouped values
        return list(hashmap.values())

solution = Solution()
print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))  # Output: [0, 1]