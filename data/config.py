class Config():
    def __init__(self):
        self._up_bound = 10
        self._low_bound = -10
        self._eos = -11
        self._input_size = 5
        self._encode_length = 7
        self._threshold = 11

    def output_range(self):
        # @TODO: problem specified, may need change
        return self._eos, self._input_size * self._up_bound

    def get_up_bound(self):
        return self._up_bound

    def get_low_bound(self):
        return self._low_bound

    def get_eos(self):
        return self._eos

    def get_input_size(self):
        return self._input_size

    def get_encoding_length(self):
        return self._encode_length

    def get_threshold(self):
        return self._threshold
