class Config():
    def __init__(self):
        # Input data element range
        self._up_bound = 1000
        self._low_bound = 1

        # end of sentence: assign an unreachable number
        self._eos = 0

        self._input_size = 5
        self._encode_length = 10
        self._threshold = 0
        self._train_data_size = 10000
        self._test_data_size = 1000

        # for variate size testing data
        self.var_input_size = 10

        # nn configs:
        self.epoch = 5
        self.h_lr = 0.02
        self.c_lr = 0.02
        self.layer_size = 2

    def output_range(self):
        # memory range
        # @TODO: problem specified, may need change
        return self._eos, 1002

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

    def get_train_data_size(self):
        return self._train_data_size

    def get_test_data_size(self):
        return self._test_data_size