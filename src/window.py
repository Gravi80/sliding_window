class Window:
    def __init__(self, collection, bucket_size, overlap_count):
        self._validate(collection, bucket_size, overlap_count)
        self._collection = collection
        self._bucket_size = bucket_size
        self._overlap_count = overlap_count
        self._window_start_index = 0
        self._window_data = None

    def slide(self):
        self._window_data = self._collection[self._window_start_index:self._window_start_index + self._bucket_size]
        if len(self._window_data) == self._bucket_size:
            self._window_start_index = self._next_window_start_index()
        return self._window_data

    def _validate(self, collection, bucket_size, overlap_count):
        collection_length = len(collection)
        if collection_length == 0:
            raise ValueError('Collection cannot be empty')
        if collection_length < bucket_size:
            raise ValueError('Bucket size should be smaller than collection size')
        if overlap_count >= bucket_size:
            raise ValueError('Overlap count should be lesser than bucket_size')

    def current_position(self):
        if self._window_start_index == 0:
            raise RuntimeError('Slide window first')
        start = (self._window_start_index - self._bucket_size) + self._overlap_count
        end = (start + self._bucket_size) - 1
        if len(self._window_data) < self._bucket_size:
            start = self._window_start_index
            end = self._collection_length() - 1
        return start, end

    def _collection_length(self):
        return len(self._collection)

    def _next_window_start_index(self):
        return (self._window_start_index + self._bucket_size) - self._overlap_count
