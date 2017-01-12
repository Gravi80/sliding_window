from __future__ import absolute_import
import unittest

from src.window import Window


class TestWindow(unittest.TestCase):
    def test_should_raise_error_for_empty_list(self):
        with self.assertRaisesRegexp(ValueError, 'Collection cannot be empty'):
            Window([], 3, 1)

    def test_should_raise_error_for_invalid_bucket_size(self):
        with self.assertRaisesRegexp(ValueError, 'Bucket size should be smaller than collection size'):
            Window([1], 3, 1)

    def test_should_raise_error_when_overlap_count_is_greater_than_bucket_size(self):
        with self.assertRaisesRegexp(ValueError, 'Overlap count should be lesser than bucket_size'):
            Window([1, 2, 3], 2, 3)

    def test_should_raise_error_when_overlap_count_is_equal_to_bucket_size(self):
        with self.assertRaisesRegexp(ValueError, 'Overlap count should be lesser than bucket_size'):
            Window([1, 2, 3], 2, 2)

    def test_should_raise_error_when_current_position_is_called_before_sliding(self):
        window = Window([1, 2, 3], 2, 1)
        with self.assertRaisesRegexp(RuntimeError, 'Slide window first'):
            window.current_position()

    # When last window contains elements less than bucket size
    def test_should_return_window_data_on_sliding(self):
        window = Window([0, 1, 2, 3, 4, 5, 6, 7], 3, 1)

        window_data = window.slide()
        self.assertEqual(window_data, [0, 1, 2])

        window_data = window.slide()
        self.assertEqual(window_data, [2, 3, 4])

        window_data = window.slide()
        self.assertEqual(window_data, [4, 5, 6])

        window_data = window.slide()
        self.assertEqual(window_data, [6, 7])

    def test_should_return_window_current_position(self):
        window = Window([0, 1, 2, 3, 4, 5, 6, 7], 3, 1)

        window.slide()
        self.assertEqual(window.current_position(), (0, 2))

        window.slide()
        self.assertEqual(window.current_position(), (2, 4))

        window.slide()
        self.assertEqual(window.current_position(), (4, 6))

        window.slide()
        self.assertEqual(window.current_position(), (6, 7))

    # When last window contains one element
    def test_should_return_window_position(self):
        window = Window([1, 2, 3, 4, 5, 6, 7], 3, 1)

        window.slide()
        self.assertEqual(window.current_position(), (0, 2))

        window.slide()
        self.assertEqual(window.current_position(), (2, 4))

        window.slide()
        self.assertEqual(window.current_position(), (4, 6))

        window.slide()
        self.assertEqual(window.current_position(), (6, 6))

    def test_should_not_change_window_data_and_position(self):
        window = Window([1, 2, 3], 2, 1)
        window.slide()
        window.slide()

        window_data = window.slide()
        self.assertEqual(window_data, [3])
        self.assertEqual(window.current_position(), (2, 2))

        window_data = window.slide()
        self.assertEqual(window_data, [3])
        self.assertEqual(window.current_position(), (2, 2))