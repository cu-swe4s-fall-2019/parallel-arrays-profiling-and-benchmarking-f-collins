import unittest
import random
import plot_gtex as pg

class TestPlotGtex(unittest.TestCase):
    def test_linear_search_empty_list(self):
        self.assertEqual(pg.linear_search(1, []), -1)

    def test_linear_search_random_list(self):
        for x in range(100):
            L = []
            location = random.randint(0, 49)
            key = 0
            for y in range(50):
                num = random.randint(5 * y, 5 * y + 4)
                if y == location:
                    key = num
                L.append(num)
            self.assertEqual(pg.linear_search(key, L), location)

if __name__ == "__main__":
    unittest.main()
