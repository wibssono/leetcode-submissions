def twoSum(nums: list[int], target: int) -> list[int] | None:
    """
    A solution to leetcode problem "1. Two Sum"
    Used a hash map to store previously seen numbers and their indices to find the target difference in a single pass.

    Complexity
    Time: O(N)
    Space: O(N)

    :type nums: list[int]
    :type target: int
    :rtype: list[int] | None
    """
    hashmap: dict[int, int] = {}
    for index, num in enumerate(nums):
        difference: int = target - num
        if difference in hashmap:
            return [hashmap[difference], index]
        elif not difference in hashmap:
            hashmap[num] = index
        else:
            raise ValueError(f"No values in List can be added to {target}")


def twoSumMemory(nums: list[int], target: int) -> list[int] | None:
    """
    A brute-force solution to leetcode problem "1. Two Sum"
    Used nested loops to check every possible pair of numbers to save memory space.

    Complexity
    Time: O(N^2)
    Space: O(1)

    :type nums: list[int]
    :type target: int
    :rtype: list[int] | None
    """
    n: int = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    raise ValueError(f"No values in List can be added to {target}")
