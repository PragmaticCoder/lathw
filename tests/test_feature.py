import unittest


class AlgoTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_some_feature(self):
        self.fail("Not Implemented")

    def tearDown(self):
        pass


if __name__ == '__main__':
    import timeit

    print(timeit.timeit("test()", setup="from __main__ import test", number=100))
    unittest.main()
