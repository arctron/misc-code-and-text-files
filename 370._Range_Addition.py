class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * length
        for update in updates:
            s = update[0]
            e = update[1]
            inc = update[2]
            ans[s] += inc
            if e < (length - 1):
                ans[e + 1] -= inc
        for i in range(1, len(ans)):
            ans[i] += ans[i-1]
        return ans
