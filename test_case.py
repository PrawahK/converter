import unittest
import main
import  pathlib as pl
import os

class Testmain(unittest.TestCase):

    def test_filecheck(self):
        path = pl.Path(main.fname)
        self.assertTrue(path.is_file())


    def test_exist(self):
        self.assertTrue(os.path.exists('./struct.json'))


