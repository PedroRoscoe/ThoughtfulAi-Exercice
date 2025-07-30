import unittest
from package import package

class TestPackageClass(unittest.TestCase):

    def test_init(self):
        p = package(100, 200, 300, 15)
        self.assertEqual(p.width, 100)
        self.assertEqual(p.height, 200)
        self.assertEqual(p.length, 300)
        self.assertEqual(p.weight, 15)
        self.assertEqual(p.is_bulky, True)  # since width*height*length >= 1000000
        self.assertEqual(p.is_heavy, False)  # since weight < 20

    def test_is_bulky(self):
        p = package(140, 140, 140, 15)
        self.assertTrue(p.is_bulky)  # since width*height*length >= 1000000

        p = package(1, 2, 3, 15)
        self.assertFalse(p.is_bulky)  # since width*height*length < 10

        p = package(200, 20, 30, 15)
        self.assertTrue(p.is_bulky)  # since width >= 150

    def test_is_heavy(self):
        p = package(10, 20, 30, 15)
        self.assertFalse(p.is_heavy)  # since weight < 20
        p = package(10, 20, 30, 20)
        self.assertTrue(p.is_heavy)  # since weight = 20
        p = package(10, 20, 30, 25)
        self.assertTrue(p.is_heavy)  # since weight >= 20

    def test_sort(self):
        p = package(10, 20, 30, 15)
        self.assertEqual(p.sort(), "STANDARD")

        p = package(200, 20, 30, 15)
        self.assertEqual(p.sort(), "SPECIAL")

        p = package(200, 200, 200, 25)
        self.assertEqual(p.sort(), "REJECTED")

        p = package(10, 20, 30, 25)
        self.assertEqual(p.sort(), "SPECIAL")

if __name__ == '__main__':
    unittest.main()