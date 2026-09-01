# LeetCode 217. Contains Duplicate

**Difficulty:** Easy  
**Problem Link:** [LeetCode - Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## Problem Description
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Approach and Analysis
For this problem, I will be discussing two different approaches in `contains_duplicate.py` to evaluate the algorithmic trade-off between execution speed and memory consumption. 

### 1. Hash Set Approach (My Original Solution)
The most efficient way to solve this problem is by converting the list into a set and comparing their lengths (`len(set(nums)) != len(nums)`). If the lengths differ, it means a duplicate was removed during the set creation.

*   **Findings:** This solution is highly optimized for speed.
*   **Stats:** Runtime = 7ms (Beats 99.35%) | Memory = 25.93 MB (Beats 42.05%)

### 2. Sorting & Pointers Approach (Memory Solution)
To optimize for space, this alternative sorts the array in-place first. It then utilizes two pointers (`subject` and `bench`) to iterate through the array and check if any adjacent values match.

*   **Findings:** While this method successfully reduces memory usage by roughly 25%, the sorting operation introduces a significant bottleneck, resulting in a massive decrease in runtime performance.
*   **Stats:** Runtime = 107ms (Beats 5.13%) | Memory = 19.19 MB (Beats 99.81%)

## Complexity

**Hash Set Approach:**
- **Time Complexity:** O(n) — Converting a list to a set requires a single traversal of the array.
- **Space Complexity:** O(n) — In the worst-case scenario (all unique elements), the hash set will store all n elements of the array.

**Sorting & Pointers Approach:**
- **Time Complexity:** O(n log n) — The dominant operation is sorting the array, which takes O(n log n) time. The subsequent pointer traversal takes O(n) time.
- **Space Complexity:** O(1) — Sorting is performed in-place (assuming standard Timsort/quicksort in-place characteristics), requiring no additional space that scales linearly with the input size.
