class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        # 2^10 * 1
        # 4^5 * 1
        # 16^2 * 4
        # 256^1 * 4
        if n < 0:
            i = -n
        else:
            i = n
        t = x
        res = 1
        while i != 1:
            r = i % 2
            if r == 0:
                res = res
            else:
                res = t * res
            i = i // 2
            t *= t
        if n < 0:
            return 1 / (t * res)
        return t * res


if __name__ == "__main__":
    print("create Solution Class")
    s = Solution()
    print("assert")
    print(s.myPow(2.0, -1))
