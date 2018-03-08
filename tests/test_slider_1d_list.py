from __future__ import absolute_import
import unittest

from window_slider.slider import Slider


class TestSlider(unittest.TestCase):
    def test_should_raise_error_for_empty_list(self):
        with self.assertRaisesRegexp(ValueError, 'List cannot be empty'):
            Slider(3, 1).fit([])

    def test_should_raise_error_for_invalid_bucket_size(self):
        with self.assertRaisesRegexp(ValueError, 'Bucket size should be smaller than list size'):
            Slider(3, 1).fit([1])

    def test_should_raise_error_when_overlap_count_is_greater_than_bucket_size(self):
        with self.assertRaisesRegexp(ValueError, 'Overlap count should be lesser than bucket_size'):
            Slider(2, 3).fit([1, 2, 3])

    def test_should_raise_error_when_overlap_count_is_equal_to_bucket_size(self):
        with self.assertRaisesRegexp(ValueError, 'Overlap count should be lesser than bucket_size'):
            Slider(2, 2).fit([1, 2, 3])

    def test_should_raise_error_when_current_position_is_called_before_sliding(self):
        window = Slider(2, 1).fit([1, 2, 3])
        with self.assertRaisesRegexp(RuntimeError, 'Slide window first'):
            window.current_position()

    # When last window contains elements less than bucket size
    def test_should_return_window_data_on_sliding(self):
        slider = Slider(3, 1).fit([0, 1, 2, 3, 4, 5, 6, 7])

        window_data = slider.slide()
        self.assertEqual(window_data, [0, 1, 2])

        window_data = slider.slide()
        self.assertEqual(window_data, [2, 3, 4])

        window_data = slider.slide()
        self.assertEqual(window_data, [4, 5, 6])

        window_data = slider.slide()
        self.assertEqual(window_data, [6, 7])

    def test_should_return_window_current_position(self):
        slider = Slider(3, 1).fit([0, 1, 2, 3, 4, 5, 6, 7])

        window_data = slider.slide()
        self.assertEqual(window_data, [0, 1, 2])
        self.assertEqual(slider.current_position(), (0, 2))

        window_data = slider.slide()
        self.assertEqual(window_data, [2, 3, 4])
        self.assertEqual(slider.current_position(), (2, 4))

        window_data = slider.slide()
        self.assertEqual(window_data, [4, 5, 6])
        self.assertEqual(slider.current_position(), (4, 6))

        window_data = slider.slide()
        self.assertEqual(window_data, [6, 7])
        self.assertEqual(slider.current_position(), (6, 7))
        self.assertTrue(slider.reached_end_of_list())

    # When last window contains one element
    def test_should_return_window_position(self):
        slider = Slider(3, 1).fit([1, 2, 3, 4, 5, 6, 7])

        slider.slide()
        self.assertEqual(slider.current_position(), (0, 2))

        slider.slide()
        self.assertEqual(slider.current_position(), (2, 4))

        slider.slide()
        self.assertEqual(slider.current_position(), (4, 6))

        slider.slide()
        self.assertEqual(slider.current_position(), (6, 6))

    def test_should_not_change_window_data_and_position(self):
        slider = Slider(2, 1).fit([1, 2, 3])
        slider.slide()
        slider.slide()

        window_data = slider.slide()
        self.assertEqual(window_data, [3])
        self.assertEqual(slider.current_position(), (2, 2))

        window_data = slider.slide()
        self.assertEqual(window_data, [3])
        self.assertEqual(slider.current_position(), (2, 2))

    def test_should_return_true_when_reached_to_end_of_list(self):
        slider = Slider(2, 1).fit([1, 2])
        slider.slide()
        slider.slide()
        self.assertTrue(slider.reached_end_of_list())

    def test_should_return_false_when_end_of_list_is_not_reached(self):
        slider = Slider(2, 1).fit([1, 2])
        slider.slide()
        self.assertFalse(slider.reached_end_of_list())
