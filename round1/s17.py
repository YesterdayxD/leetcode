class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "kjl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if not digits:
            return []
        res = [""]
        for i in digits:
            size = len(res)
            cur = table[i]
            for _ in range(size):
                tmp = res.pop(0)
                for t in cur:
                    res.append(tmp + t)

        return res
