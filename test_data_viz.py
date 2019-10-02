import unittest
import os
import data_viz as dv


class TestDataViz(unittest.TestCase):
    def test_boxplot_file_name_none(self):
        self.assertIsNone(dv.boxplot(None, None, None, None, None, None), None)

    def test_boxplot_file_created(self):
        outfile = "output.png"
        dv.boxplot([[1, 2, 3, 4, 5]], outfile, "Test Title", ["Label"],
                   "X-axis", "Y-axis")
        self.assertTrue(os.path.exists(outfile))
        os.remove(outfile)

    def test_boxplot_file_created_two_lists(self):
        outfile = "output.png"
        dv.boxplot([[1, 2, 3, 4, 5], [2, 3, 4, 5, 7]], outfile, "Test Title",
                   ["Label 1", "Label 2"], "X-axis", "Y-axis")
        self.assertTrue(os.path.exists(outfile))
        os.remove(outfile)

    def test_histogram_file_name_none(self):
        self.assertIsNone(dv.histogram(None, None), None)

    def test_histogram_file_created(self):
        outfile = "output.png"
        dv.histogram([1, 2, 3, 4, 5], outfile)
        self.assertTrue(os.path.exists(outfile))
        os.remove(outfile)

    def test_combo_file_name_none(self):
        self.assertIsNone(dv.combo(None, None), None)

    def test_combo_file_created(self):
        outfile = "output.png"
        dv.combo([1, 2, 3, 4, 5], outfile)
        self.assertTrue(os.path.exists(outfile))
        os.remove(outfile)


if __name__ == "__main__":
    unittest.main()
