import unittest 

from boggle import *
#other ways of writing this:
#import boggle 
#from boggle import make_grid, add,..

#TestBoggle inherits from TestCase. The below tests will run by unittest for all functions within this TestBoggle class.
from string import ascii_uppercase
class TestBoggle(unittest.TestCase):
    
    # must put in "self"
 
        
    def test_empty_grid(self):
        grid = make_grid(0, 0)
        self.assertEqual(grid, {})
        
    def test_non_empty_grid(self):
        grid = make_grid(2, 2)
        self.assertEqual(len(grid), 4)
        
    def test_grid_has_upper_case_letters(self):
        grid = make_grid(2, 2)
        for c in grid.values():
            self.assertIn(c, ascii_uppercase)        
        
        
            