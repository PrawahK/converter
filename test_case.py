import unittest
import main2
import pathlib as pl
import os


class Testmain(unittest.TestCase):

    def test_processed_output_exist(self):
        """To test if the output Json file exist after running the main file."""

        self.assertTrue(os.path.exists('./struct.json'))

    def test_output_exsist(self):
        "Check if the output file is attached"
        self.assertTrue(os.path.exists('./output.txt'))
        print(main2.upload_csv())





