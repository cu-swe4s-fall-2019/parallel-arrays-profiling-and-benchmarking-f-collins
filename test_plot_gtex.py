import unittest
import random
import plot_gtex as pg


class TestPlotGtex(unittest.TestCase):
    def test_linear_search_empty_list(self):
        self.assertEqual(pg.linear_search(1, []), -1)

    def test_linear_search_random_list(self):
        for x in range(100):
            L = []
            for y in range(50):
                num = random.randint(5 * y, 5 * y + 4)
                L.append(num)
            location = random.randint(0, 49)
            key = L[location]
            self.assertEqual(pg.linear_search(key, L), location)

    def test_binary_search_empty_list(self):
        self.assertEqual(pg.binary_search(1, []), -1)

    def test_binary_search_random_list(self):
        for x in range(100):
            L = []
            for y in range(50):
                num = random.randint(5 * y, 5 * y + 4)
                L.append(num)
            location = random.randint(0, 49)
            key = L[location]
            self.assertEqual(pg.binary_search(key, L), location)


if __name__ == "__main__":
    unittest.main()
