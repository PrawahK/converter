import unittest
import main2
import pathlib as pl
import os

class Testmain(unittest.TestCase):

    def test_exist(self):
        """To test if the output Json file exist after running the main file."""

        self.assertTrue(os.path.exists('./struct.json'))


