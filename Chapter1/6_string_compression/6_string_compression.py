import unittest
import time

def compress_string(string):
    compress = []
    counter = 0
    for i in range(0, len(string)):
        if (i>0) & (string[i-1]!=string[i]):
            compress.append(string[i-1] + str(counter))
            counter = 1
        else:
            counter = counter+1
    if counter:
        compress.append(string[-1] + str(counter))
    return min(string, "".join(compress), key =len)


class Test(unittest.TestCase):
    test_cases = (
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    )
    testable_functions = (
        compress_string,
    )

    def test_string_compression(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for test_string, expected in self.test_cases:
                    assert (
                                   f(test_string) == expected
                    ),f"{func.__name__} is failed for {text}"
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")

if __name__ == "__main__":
    unittest.main()