import unittest
from models.munro import Munro

class TestMunro(unittest.TestCase):
    
    def setUp(self):
        self.task = Munro("Ben More", "3000 ft", false, "Mull")
    
    
    def test_munro_has_name(self):
        self.assertEqual("Ben More", self.munro.name)