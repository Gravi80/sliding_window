class Slider:
    def __init__(self, window_size, overlap_count):
        self._window_size = window_size
        self._overlap_count = overlap_count
        self._window_start_index = 0
        self._window_data = None
        self._data = None

    def fit(self, data):
        self._data = self._validate(data)
        return self

    def slide(self):
        self._window_data = self._data[self._window_start_index:self._window_start_index + self._window_size]
        if len(self._window_data) == self._window_size:
            self._window_start_index = self._next_window_start_index()
        return self._window_data

    def _validate(self, data):
        list_length = len(data)
        if list_length == 0:
            raise ValueError('List cannot be empty')
        if list_length < self._window_size:
            raise ValueError('Bucket size should be smaller than list size')
        if self._overlap_count >= self._window_size:
            raise ValueError('Overlap count should be lesser than bucket_size')
        return data

    def current_position(self):
        if self._window_start_index == 0:
            raise RuntimeError('Slide window first')
        start = (self._window_start_index - self._window_size) + self._overlap_count
        end = (start + self._window_size) - 1
        if len(self._window_data) < self._window_size:
            start = self._window_start_index
            end = self._list_length() - 1
        return start, end

    def reached_end_of_list(self):
        return len(self._window_data) < self._window_size

    def _list_length(self):
        return len(self._data)

    def _next_window_start_index(self):
        return (self._window_start_index + self._window_size) - self._overlap_count
