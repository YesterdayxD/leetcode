class Solution:
    def isValid(self, s: str) -> bool:
        a = ["1", ]
        r = len(s) % 2
        if r != 0:
            return False
        for i in s:
            if a[-1] == '(' and i == ')':
                a.pop()
            elif a[-1] == '[' and i == ']':
                a.pop()
            elif a[-1] == '{' and i == '}':
                a.pop()
            else:
                a.append(i)

        return len(a) == 1
