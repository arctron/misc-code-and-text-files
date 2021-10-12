class Solution:
    def lengthOfLongestSubstringKDistinct(self, st: str, k: int) -> int:
        s = 0
        e = 0
        ans = 0
        letters = {}
        cur_k = 0
        while e < len(st):
            if st[e] not in letters:
                cur_k += 1
                letters[st[e]] = 0
            letters[st[e]] += 1
            if cur_k <= k:
                ans = max(ans, e - s + 1)
            else:
                while cur_k > k and s < len(st):
                    letters[st[s]] -= 1
                    if letters[st[s]] == 0:
                        cur_k -= 1
                        del letters[st[s]]
                    s += 1
            e += 1
        return ans
