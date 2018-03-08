class Slider:
    def __init__(self, window_size, overlap_count, window_data_wrapper_class=None):
        self._window_size = window_size
        self._overlap_count = overlap_count
        self._window_start_index = 0
        self._window_data = None
        self._data = None
        self._window_data_wrapper_class = window_data_wrapper_class

    def fit(self, data):
        self._data = self._validate(data)
        return self

    def slide(self):
        if self._1d_array(self._data):
            self._1d_array_window()
        else:
            self._2d_array_window()
        if self._window_data_wrapper_class:
            return self._window_data_wrapper_class(self._window_data)
        return self._window_data

    def _validate(self, data):
        if not (self._1d_array(data) or self._2d_array(data)):
            raise ValueError('Only 1D and 2D numpy array supported')
        list_length = self._data_length(data)
        if list_length == 0:
            raise ValueError('List cannot be empty')
        if list_length < self._window_size:
            raise ValueError('Bucket size should be smaller than list size')
        if self._overlap_count >= self._window_size:
            raise ValueError('Overlap count should be lesser than bucket_size')
        return data

    def _data_length(self, data):
        return len(data) if self._1d_array(data) else len(data[0])

    def _1d_array(self, array):
        return len(array.shape) == 1

    def _2d_array(self, array):
        return len(array.shape) == 2

    def current_position(self):
        if self._window_start_index == 0:
            raise RuntimeError('Slide window first')
        start = (self._window_start_index - self._window_size) + self._overlap_count
        end = (start + self._window_size) - 1
        end, start = self._handle_last_window(end, start)
        return start, end

    def _handle_last_window(self, end, start):
        data = self._window_data if self._1d_array(self._window_data) else self._window_data[0]
        if len(data) < self._window_size:
            start = self._window_start_index
            end = self._list_length() - 1
        return end, start

    def reached_end_of_list(self):
        data = self._window_data if self._1d_array(self._window_data) else self._window_data[0]
        return (len(data) < self._window_size) or (self._window_start_index == self._list_length())

    def _list_length(self):
        return len(self._data) if self._1d_array(self._window_data) else len(self._data[0])

    def _next_window_start_index(self):
        return (self._window_start_index + self._window_size) - self._overlap_count

    def _1d_array_window(self):
        self._window_data = self._data[self._window_start_index:self._window_start_index + self._window_size]
        if len(self._window_data) == self._window_size:
            self._window_start_index = self._next_window_start_index()

    def _2d_array_window(self):
        self._window_data = self._data[:, self._window_start_index:self._window_start_index + self._window_size]
        if len(self._window_data[0]) == self._window_size:
            self._window_start_index = self._next_window_start_index()
