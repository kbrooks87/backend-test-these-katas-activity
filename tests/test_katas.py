import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        #self.fail("TODO: Write add unit test")
        result = katas.add(10, 5)
        self.assertEqual(result, 15)

    def test_multiply(self):
        #self.fail("TODO: Write multiply unit test")
        result = katas.multiply(6, 5)
        self.assertEqual(result, 30)

    def test_power(self):
        #self.fail("TODO: Write power unit test")
        result = katas.power(2, 3)
        self.assertEqual(result, 8)

    def test_factorial(self):
        #self.fail("TODO: Write factorial unit test")
        result = katas.factorial(4)
        self.assertEqual(result, 24)

    def test_fibonacci(self):
        #self.fail("TODO: Write fibonacci unit test")
        result = katas.fibonacci(10)
        self.assertEqual(result, 34)


if __name__ == '__main__':
    unittest.main()
