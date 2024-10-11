import unittest
from collections import Counter
import numpy as np
import time
def is_one_edit(s1, s2):
    if abs(len(s1)-len(s2))>=2:
        return False
    if len(s1) == len(s2):
        return one_edit_replacement(s1, s2)
    if abs(len(s1) - len(s2))==1:
        return one_edit_insert_del(s1, s2)
def one_edit_insert_del(s1,s2):
    big_str = s1 if len(s1)>len(s2) else s2
    small_str = s1 if len(s1)<len(s2) else s2
    i,j = 0, 0
    edit = False
    while i< len(big_str) and j<len(small_str):
        if big_str[i] != small_str[j]:
            if edit:
                return False
            edit = True
            i += 1
        else:
            i += 1
            j += 1
    return True
def one_edit_replacement(s1, s2):
    if s1==s2:
        return True
    cnt = Counter()
    for ch in s1:
        cnt[ch] += 1
    for ch in s2:
        if cnt.get(ch) is not None:
            cnt[ch] -= 1
        else:
            cnt[ch] += 1
    #print(cnt)
    #print(cnt.values())
    return np.sum(list(cnt.values()))==2


class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]

    testable_functions = [is_one_edit]

    def test_one_away(self):

        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert (
                            f(text_a, text_b) == expected
                    ), f"{f.__name__} is failed for {text_a},{text_b}"
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()