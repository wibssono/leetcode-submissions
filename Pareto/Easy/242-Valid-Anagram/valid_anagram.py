def isAnagram(s: str, t: str) -> bool:
    """
    My original solution to leetcode problem "242. Valid Anagram"
    Used sorted string and compare each letter to find a difference

    Stats:
    Runtime = 31ms | Beats 6.16%
    Memory = 13.52MB | Beats 19.82%

    :type s: str
    :type t: str
    :rtype: bool
    """
    length_s: int = len(s)
    length_t: int = len(t)
    if length_s != length_t:
        return False

    subject: list[str] = sorted(s)
    print(s)
    test: list[str] = sorted(t)
    print(t)

    bench = 0

    while bench < (length_s):
        print(f"Subject = {s[bench]} and bench = {t[bench]}")
        if subject[bench] != test[bench]:
            return False
        bench += 1
    return True


def isAnagramTwoHashMap(s: str, t: str) -> bool:
    """
    Best memory solution to leetcode problem "242. Valid Anagram"
    Used hashmaps to find a matches in each letter

    Stats:
    12.2 Mb

    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    dict1 = {}
    dict2 = {}
    for x in s:
        if x in dict1:
            dict1[x] += 1
        else:
            dict1[x] = 1
    for y in t:
        if y in dict2:
            dict2[y] += 1
        else:
            dict2[y] = 1

    return dict1 == dict2


def isAnagramHashmap(s: str, t: str) -> bool:
    """
    Popular solution to leetcode problem "242. Valid Anagram" that I modified a bit
    Used hashmaps to find a matches in each letter

    Stats:
    Runtime = 15ms | Beats 85.88%
    Memory = 12.70MB | Beats 49.70%

    :type s: str
    :type t: str
    :rtype: bool
    """
    lettermap: dict[str, int] = {}
    for letter in s:
        if letter in lettermap:
            lettermap[letter] += 1
        else:
            lettermap[letter] = 1
    print(lettermap)
    for letter in t:
        if letter in lettermap and lettermap[letter] > 0:
            lettermap[letter] -= 1
        else:
            return False
    return True
