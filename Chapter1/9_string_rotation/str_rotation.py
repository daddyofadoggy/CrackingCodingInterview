# O(N)
import unittest
def str_rotation(s1, s2):
    if len(s1)!=len(s2):
        return False
    if s1==s2:
        return False
    return s2 in s1*2


class Test(unittest.TestCase):

    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.test_cases:
            actual = str_rotation(s1, s2)
            print(actual)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()