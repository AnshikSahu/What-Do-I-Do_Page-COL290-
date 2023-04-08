import unittest
import functions

class Test_Movies(unittest.TestCase):
    def test_movie_details_full_non_existing_movies(self):
        with self.assertRaises(ValueError):
            movie=functions.movie_details_full("1234")
