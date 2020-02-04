class Solution:
    def searchRange(self, nums, target):
        def searchLeft(left, right):
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    if pivot - 1 > -1 and nums[pivot - 1] == target:
                        right = pivot - 1
                    else:
                        return pivot

                else:
                    if nums[pivot] > target:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        def searchRight(left, right):
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    if pivot + 1 < n  and nums[pivot + 1] == target:
                        left = pivot + 1
                    else:
                        return pivot

                else:
                    if nums[pivot] > target:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        n = len(nums)
        left_index = searchLeft(0, n - 1)
        right_index = searchRight(0, n - 1)
        return [left_index, right_index]


if __name__ == "__main__":
    print("create Solution Class")
    s = Solution()
    print("assert")
    print(s.searchRange([2, 2], 2))
