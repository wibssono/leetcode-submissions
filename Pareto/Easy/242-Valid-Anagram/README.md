# LeetCode 242. Valid Anagram

**Difficulty:** Easy  
**Problem Link:** [LeetCode - Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

## Approach and Analysis

For this problem, I will be discussing four different approaches to evaluate the algorithmic trade-offs between execution speed, memory consumption, and practical scalability.

### 1. Single Hashmap Approach (Modified Popular Solution)

This approach uses a single dictionary to count character frequencies in string `s`, and then decrements those counts while iterating through string `t`.

* **Findings:** The most algorithmically sound solution. It guarantees optimal linear time and handles unbounded character sets safely without creating completely new string copies in memory.
* **Stats:** Runtime = 15ms (Beats 85.88%) | Memory = 12.70 MB (Beats 49.70%)

### 2. Two Hashmaps Approach (Best Memory Solution)

This approach builds two separate dictionaries—one for each string—and compares them directly using Python's built-in dictionary equality check.

* **Findings:** While it technically allocates two dictionaries instead of one, Python optimizes the `==` comparison, making it fast and easy to read.
* **Stats:** Runtime = 12ms | Memory = 12.2 MB

### 3. Sorting Approach (My Original Solution)

This alternative sorts both strings first. It then uses a pointer to iterate through the arrays and checks if the characters at each index match.

* **Findings:** While conceptually simple, the sorting operation introduces a significant bottleneck. It results in slower execution and higher memory usage due to Python creating new list copies of the sorted strings.
* **Stats:** Runtime = 31ms (Beats 6.16%) | Memory = 13.52 MB (Beats 19.82%)

## Complexity

**Single Hashmap / Two Hashmaps Approaches:**

* **Time Complexity:** O(n) — Requires linear traversal of the strings to count character frequencies.
* **Space Complexity:** O(1) — Assuming a fixed character set (like 26 English lowercase letters), the dictionary size remains constant.

**Sorting Approach:**

* **Time Complexity:** O(n log n) — The dominant operation is sorting the strings via Timsort.
* **Space Complexity:** O(n) — Python strings are immutable, so `sorted()` allocates brand new lists of size n in memory.
