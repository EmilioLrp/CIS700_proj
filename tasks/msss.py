"""MSSS NTM model."""
import pickle as pk

import torch
from attr import attrs, attrib, Factory
from torch import nn
from torch import optim

from data.config import Config
from data.encoder import encoder
from ntm.aio import EncapsulatedNTM


# Generator of randomized test sequences
def dataloader(num_batches,
               batch_size,
               data,
               pointer,
               seq_length,
               seq_width):
    """Generator of random sequences for the copy task.

    Creates random batches of "bits" sequences.

    All the sequences within each batch have the same length.
    The length is [`min_len`, `max_len`]

    :param num_batches: Total number of batches to generate.
    :param batch_size: Batch size.
    :param seq_width: The width of each item in the sequence.

    NOTE: The input width is `seq_width + 1`, the additional input
    contain the delimiter.
    """
    # for batch_num in range(num_batches):
    #     # All batches have the same sequence length
    #     seq_len = random.randint(min_len, max_len)
    #     seq = np.random.binomial(1, 0.5, (seq_len, batch_size, seq_width))
    #     seq = torch.from_numpy(seq)
    #
    #     # The input includes an additional channel used for the delimiter
    #     inp = torch.zeros(seq_len + 1, batch_size, seq_width + 1)
    #     inp[:seq_len, :, :seq_width] = seq
    #     inp[seq_len, :, seq_width] = 1.0  # delimiter in our control channel
    #     outp = seq.clone()
    #
    #     yield batch_num + 1, inp.float(), outp.float()

    # @TODO dimension checking!!!
    (x, y) = data
    length = len(x)
    for batch_num in range(num_batches):
        inp = torch.zeros(seq_length, batch_size, seq_width)
        oup = torch.zeros(seq_length, batch_size, seq_width)
        for i in range(batch_size):
            if pointer >= length:
                break
            else:
                inp[:, i, :] = encode(x[pointer])
                oup[:, i, :] = encode(y[pointer])
                # inp = encode(x[pointer]).unsqueeze(dim=1)
                # oup = encode(y[pointer]).unsqueeze(dim=1)
                # yield batch_num + 1, inp.float(), oup.float()
                pointer += 1
        yield batch_num + 1, inp.float(), oup.float()
        # if pointer >= length:
        #     break
        # else:
        #     pointer += 1
        #     yield batch_num + 1, x[pointer - 1], y[pointer - 1]


def encode(inarr):
    conf = Config()
    result = []
    for element in inarr:
        result.append(encoder(element, conf.get_threshold(), conf.get_encoding_length()))
    return torch.stack(result, dim=0)


@attrs
class MSSSParams(object):
    # specified = attrib(default=Factory(specified_param))
    # @TODO: change them when testing
    conf = Config()
    M = conf.get_encoding_length()
    m_min, m_max = conf.output_range()
    N = m_max - m_min + 1
    seq_length = conf.get_input_size() + 1  # number of elements in the input sequence
    var_seq_length = conf.var_input_size + 1
    elem_size = conf.get_encoding_length()  # length of the vector of each element in the input sequence
    total_data_size = conf.get_train_data_size()
    # total_data_size = conf.get_test_data_size()
    batch_len = conf.batch_size
    batch_num = total_data_size / batch_len

    name = attrib(default="msss-task")
    controller_size = attrib(default=100, convert=int)
    controller_layers = attrib(default=conf.layer_size, convert=int)
    num_heads = attrib(default=1, convert=int)
    sequence_width = attrib(default=elem_size, convert=int)
    # sequence_min_len = attrib(default=1, convert=int)
    # sequence_max_len = attrib(default=20, convert=int)
    memory_n = attrib(default=N, convert=int)
    memory_m = attrib(default=M, convert=int)
    num_batches = attrib(default=batch_num, convert=int)
    batch_size = attrib(default=batch_len, convert=int)
    rmsprop_lr = attrib(default=1e-4, convert=float)
    rmsprop_momentum = attrib(default=0.9, convert=float)
    rmsprop_alpha = attrib(default=0.95, convert=float)


@attrs
class MSSSParamsTest(object):
    # specified = attrib(default=Factory(specified_param))
    # @TODO: change them when testing
    conf = Config()
    M = conf.get_encoding_length()
    m_min, m_max = conf.output_range()
    N = m_max - m_min + 1
    seq_length = conf.get_input_size() + 1  # number of elements in the input sequence
    var_seq_length = conf.var_input_size + 1
    elem_size = conf.get_encoding_length()  # length of the vector of each element in the input sequence
    total_data_size = conf.get_test_data_size()
    batch_len = conf.batch_size
    batch_num = total_data_size / batch_len

    name = attrib(default="msss-task")
    controller_size = attrib(default=100, convert=int)
    controller_layers = attrib(default=conf.layer_size, convert=int)
    num_heads = attrib(default=1, convert=int)
    sequence_width = attrib(default=elem_size, convert=int)
    # sequence_min_len = attrib(default=1, convert=int)
    # sequence_max_len = attrib(default=20, convert=int)
    memory_n = attrib(default=N, convert=int)
    memory_m = attrib(default=M, convert=int)
    num_batches = attrib(default=batch_num, convert=int)
    batch_size = attrib(default=batch_len, convert=int)
    rmsprop_lr = attrib(default=1e-4, convert=float)
    rmsprop_momentum = attrib(default=0.9, convert=float)
    rmsprop_alpha = attrib(default=0.95, convert=float)


@attrs
class MSSSParamsVar(object):
    # specified = attrib(default=Factory(specified_param))
    # @TODO: change them when testing
    conf = Config()
    M = conf.get_encoding_length()
    m_min, m_max = conf.output_range()
    N = m_max - m_min + 1
    seq_length = conf.get_input_size() + 1  # number of elements in the input sequence
    var_seq_length = conf.var_input_size + 1
    elem_size = conf.get_encoding_length()  # length of the vector of each element in the input sequence
    total_data_size = conf.get_test_data_size()
    batch_len = conf.batch_size
    batch_num = total_data_size / batch_len

    name = attrib(default="msss-task")
    controller_size = attrib(default=100, convert=int)
    controller_layers = attrib(default=conf.layer_size, convert=int)
    num_heads = attrib(default=1, convert=int)
    sequence_width = attrib(default=elem_size, convert=int)
    # sequence_min_len = attrib(default=1, convert=int)
    # sequence_max_len = attrib(default=20, convert=int)
    memory_n = attrib(default=N, convert=int)
    memory_m = attrib(default=M, convert=int)
    num_batches = attrib(default=batch_num, convert=int)
    batch_size = attrib(default=batch_len, convert=int)
    rmsprop_lr = attrib(default=1e-4, convert=float)
    rmsprop_momentum = attrib(default=0.9, convert=float)
    rmsprop_alpha = attrib(default=0.95, convert=float)
#
# To create a network simply instantiate the `:class:CopyTaskModelTraining`,
# all the components will be wired with the default values.
# In case you'd like to change any of defaults, do the following:
#
# > params = CopyTaskParams(batch_size=4)
# > model = CopyTaskModelTraining(params=params)
#
# Then use `model.net`, `model.optimizer` and `model.criterion` to train the
# network. Call `model.train_batch` for training and `model.evaluate`
# for evaluating.
#
# You may skip this alltogether, and use `:class:CopyTaskNTM` directly.
#

def load_train_data():
    with open("data/train.txt", "rb") as f:
        train_data = pk.load(f)
    return train_data


@attrs
class MSSSModelTraining(object):
    params = attrib(default=Factory(MSSSParams))
    net = attrib()
    dataloader = attrib()
    criterion = attrib()
    optimizer = attrib()
    train_data = load_train_data()
    trained_index = 0

    @net.default
    def default_net(self):
        # We have 1 additional input for the delimiter which is passed on a
        # separate "control" channel
        net = EncapsulatedNTM(self.params.sequence_width, self.params.sequence_width,
                              self.params.controller_size, self.params.controller_layers,
                              self.params.num_heads,
                              self.params.memory_n, self.params.memory_m)
        return net

    @dataloader.default
    def default_dataloader(self):
        # return dataloader(self.params.num_batches, self.params.batch_size,
        #                   self.params.sequence_width,
        #                   self.params.sequence_min_len, self.params.sequence_max_len)
        return dataloader(self.params.num_batches, self.params.batch_size, self.train_data, self.trained_index,
                          self.params.seq_length, self.params.sequence_width)

    @criterion.default
    def default_criterion(self):
        return nn.MSELoss(reduction='mean')

    @optimizer.default
    def default_optimizer(self):
        # return optim.RMSprop(self.net.parameters(),
        #                      momentum=self.params.rmsprop_momentum,
        #                      alpha=self.params.rmsprop_alpha,
        #                      lr=self.params.rmsprop_lr)
        return optim.Adam(self.net.parameters())


def load_test2_data():
    with open("data/test_var.txt", "rb") as f:
        train_data = pk.load(f)
    return train_data


@attrs
class MSSSModelTesting2(object):
    params = attrib(default=Factory(MSSSParamsVar))
    net = attrib()
    dataloader = attrib()
    criterion = attrib()
    optimizer = attrib()
    test2_data = load_test2_data()
    trained_index = 0

    @net.default
    def default_net(self):
        # We have 1 additional input for the delimiter which is passed on a
        # separate "control" channel
        net = EncapsulatedNTM(self.params.sequence_width, self.params.sequence_width,
                              self.params.controller_size, self.params.controller_layers,
                              self.params.num_heads,
                              self.params.memory_n, self.params.memory_m)
        return net

    @dataloader.default
    def default_dataloader(self):
        # return dataloader(self.params.num_batches, self.params.batch_size,
        #                   self.params.sequence_width,
        #                   self.params.sequence_min_len, self.params.sequence_max_len)
        return dataloader(self.params.num_batches, self.params.batch_size, self.test2_data, self.trained_index,
                          self.params.var_seq_length, self.params.sequence_width)

    @criterion.default
    def default_criterion(self):
        return nn.MSELoss(reduction='mean')

    @optimizer.default
    def default_optimizer(self):
        # return optim.RMSprop(self.net.parameters(),
        #                      momentum=self.params.rmsprop_momentum,
        #                      alpha=self.params.rmsprop_alpha,
        #                      lr=self.params.rmsprop_lr)
        return optim.Adam(self.net.parameters())


def load_test_data():
    with open("data/test.txt", "rb") as f:
        train_data = pk.load(f)
    return train_data


@attrs
class MSSSModelTesting(object):
    params = attrib(default=Factory(MSSSParams))
    net = attrib()
    dataloader = attrib()
    criterion = attrib()
    optimizer = attrib()
    test_data = load_test_data()
    trained_index = 0

    @net.default
    def default_net(self):
        # We have 1 additional input for the delimiter which is passed on a
        # separate "control" channel
        net = EncapsulatedNTM(self.params.sequence_width, self.params.sequence_width,
                              self.params.controller_size, self.params.controller_layers,
                              self.params.num_heads,
                              self.params.memory_n, self.params.memory_m)
        return net

    @dataloader.default
    def default_dataloader(self):
        # return dataloader(self.params.num_batches, self.params.batch_size,
        #                   self.params.sequence_width,
        #                   self.params.sequence_min_len, self.params.sequence_max_len)
        return dataloader(self.params.num_batches, self.params.batch_size, self.test_data, self.trained_index,
                          self.params.seq_length, self.params.sequence_width)

    @criterion.default
    def default_criterion(self):
        return nn.MSELoss(reduction='mean')

    @optimizer.default
    def default_optimizer(self):
        # return optim.RMSprop(self.net.parameters(),
        #                      momentum=self.params.rmsprop_momentum,
        #                      alpha=self.params.rmsprop_alpha,
        #                      lr=self.params.rmsprop_lr)
        return optim.Adam(self.net.parameters())
