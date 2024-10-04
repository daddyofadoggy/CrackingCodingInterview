import unittest
from collections import Counter


def is_unique_cnt(str1):
    if len(str1)>128:
        return False
    cnt = Counter()
    for ch in str1:
        if cnt[ch]>0:
            return False
        cnt[ch] += 1
    return True

def is_unique_set(str1):
    return len(set(str1)) == len(str1)

def is_unique_bitmap(str1):
    if len(str1)>128:
        return False
    mask =0
    for ch in str1:
        if (mask & (1<<ord(ch))) > 0:
            return False
        mask |= 1<< ord(ch)
    return True


class Test(unittest.TestCase):
    data = (
        ('abcd', True),
        ('def', True),
        ('abcb', False),
    )

    test_functions = [
        is_unique_cnt,
        is_unique_set,
        is_unique_bitmap
    ]
    def test_cases(self):

        for text, expected in self.data:
            for func in self.test_functions:
                assert (
                        func(text) == expected
                ), f"{func.__name__} is failed for {text}"


if __name__ == "__main__":
    unittest.main()