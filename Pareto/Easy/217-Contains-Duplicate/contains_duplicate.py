def containsDuplicateMySolution(nums: list[int]) -> bool:
    """
    My original solution to the '217. Contains Duplicate' leet code problem.
    subject used a set to get the unique values of the list before comparing them.

    Stats:
    Runtime = 7ms | Beats 99.35%
    Memory = 25.93 mb | Beats 42.05%

    :type nums: List[int]
    :rtype: bool
    """
    unique_key: set[int] = set(nums)
    return len(unique_key) != len(nums)


def containsDuplicateMemorySolution(nums: list[int]) -> bool:
    """
    Memory solution to the '217. Contains Duplicate' leet code problem.
    This used the list.sort() before checking each if there's any duplicate by comparing the subject and bench

    Stats:
    Runtime = 107ms | Beats 5.13%
    Memory = 19.19MB | Beats 99.81%

    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    subject: int = 0
    bench: int = subject + 1
    while bench < len(nums) and subject < len(nums):
        if nums[subject] == nums[bench]:
            return True
        subject += 1
        bench += 1
    return False
