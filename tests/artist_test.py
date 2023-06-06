import unittest
from models.artist import Artist

class TestTask(unittest.TestCase):
    
    def setUp(self):
        self.artist = Artist("Godspeed You Black Emperor")
    
    
    # def test_artist_has_name(self):
        # self.assertEqual("Walk Dog", self.task.description)
        
