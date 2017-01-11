from __future__ import absolute_import
import unittest

from src.window import Window


class TestWindow(unittest.TestCase):
    # NOTE: its a basic setup will add meaningful tests
    def test_should_pass(self):
        collection = [0, 1, 2, 3, 4, 5, 6, 7]
        bucket_size = 3
        overlap_count = 1
        window = Window(collection, bucket_size, overlap_count)
        window_data = window.slide()
        self.assertEqual(window_data, [0, 1, 2])
        self.assertEqual(window.current_position(), (0, 2))
        window_data = window.slide()
        self.assertEqual(window_data, [2, 3, 4])
        self.assertEqual(window.current_position(), (2, 4))
        window_data = window.slide()
        self.assertEqual(window_data, [4, 5, 6])
        self.assertEqual(window.current_position(), (4, 6))
        window_data = window.slide()
        self.assertEqual(window_data, [6, 7])
        self.assertEqual(window.current_position(), (6, 7))
        window_data = window.slide()
        self.assertEqual(window_data, [6, 7])
        self.assertEqual(window.current_position(), (6, 7))
