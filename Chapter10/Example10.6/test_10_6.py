import unittest
import sys
import import_ipynb
from Volume_of_Solid import *

class Test(unittest.TestCase):
    
    def test_function(self):
        self.assertEqual(f(9),3)

    def test_vol_solid(self):
        self.assertAlmostEqual(vol_solid(f,0,1),1.569,3)


if __name__ == '__main__':
    unittest.main()
