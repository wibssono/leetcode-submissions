# LeetCode 1. Two Sum

**Difficulty:** Easy  
**Problem Link:** [LeetCode - Two Sum](https://leetcode.com/problems/two-sum/)

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have *exactly* one solution, and you may not use the same element twice. You can return the answer in any order.

## Approach and Analysis

For this problem, I will be discussing two different approaches to evaluate the algorithmic trade-offs between execution speed, memory consumption, and practical scalability based on your provided solutions.

### 1. Hashmap Approach (Optimized Solution)

This approach uses a single dictionary to store previously seen numbers and their indices. While iterating through `nums`, it calculates the required difference (`target - num`) and checks if it already exists in the dictionary.

* **Findings:** The most algorithmically sound solution. It guarantees optimal linear time by trading off a small amount of memory to achieve O(1) lookups, avoiding the need to repeatedly scan the array.
* **Stats:** Runtime is exceptionally fast as it only requires a single pass. Memory usage is slightly higher due to the dictionary allocation.

### 2. Brute Force Approach (Best Memory Solution)

This alternative uses nested loops to check every possible pair of numbers in the array. It compares the sum of each pair directly against the target.

* **Findings:** While conceptually simple and memory-efficient (since no additional data structures are created), the nested loops introduce a significant bottleneck. It results in slower execution times, especially for larger arrays.
* **Stats:** Runtime is significantly slower due to the quadratic scaling. Memory is highly optimized and remains flat regardless of input size.

## Complexity

**Hashmap Approach:**

* **Time Complexity:** O(n) — Requires a single linear traversal of the array. Dictionary lookups and insertions operate in O(1) average time.
* **Space Complexity:** O(n) — The dictionary stores at most `n` elements in the worst-case scenario (when the pair is at the very end of the array).

**Brute Force Approach:**

* **Time Complexity:** O(n²) — The dominant operation is the nested loop, which compares every combination of elements.
* **Space Complexity:** O(1) — No extra memory is allocated; only pointers `i` and `j` are used.
