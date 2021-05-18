class Config():
    def __init__(self):
        self.up_bound = 10
        self.low_bound = -10
        self.eos = -11
        self.input_size = 5

    def output_range(self):
        # @TODO: problem specified, may need change
        return self.low_bound, self.input_size * self.up_bound
