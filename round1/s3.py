class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #  build-in function ord (char -> ASCII)
        #  slide window
        record = [-1] * 256
        length = len(s)
        left = -1
        res = 0
        for i in range(length):
            left = max(left, record[ord(s[i])])
            record[ord(s[i])] = i
            res = max(res, i - left)

        return res
