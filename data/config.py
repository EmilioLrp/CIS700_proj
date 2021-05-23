class Config():
    def __init__(self):
        # Input data element range
        self._up_bound = 10
        self._low_bound = 0

        # end of sentence: assign an unreachable number
        self._eos = -1

        self._input_size = 6
        self._encode_length = 5
        self._threshold = 1
        self._train_data_size = 10000
        self._test_data_size = 1000

        # for variate size testing data
        self.var_input_size = 10

        # model 1 nn configs:
        '''
        self.epoch = 10
        self.h_lr = 0.03
        self.c_lr = 0.07
        self.layer_size = 2
        '''
        # model 2 nn configs:
        '''
        self.epoch = 10
        self.h_lr = 0.01
        self.c_lr = 0.05
        self.layer_size = 2
       
        '''
        # model 3 nn configs:
        self.epoch = 10
        self.h_lr = 0.03
        self.c_lr = 0.07
        self.layer_size = 3


    def output_range(self):
        # memory range
        # @TODO: problem specified, may need change
        return self._eos, self.var_input_size * self._up_bound

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