class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        我们可以将该问题形式化地描述为：给定若干个数字，
        将其组合为一个整数。如何将这些数字重新排列，以得到下一个更大的整数。
        如 123 下一个更大的数为 132。如果没有更大的整数，则输出最小的整数。
        """

        if len(nums) <= 1:
            return

        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1

        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        if i >= 0:
            while nums[i] >= nums[k]:
                k -= 1

            nums[i], nums[k] = nums[k], nums[i]

        if j == 0:
            return nums.reverse()

        nums[j:] = nums[len(nums) - 1:j - 1:-1]

        return
