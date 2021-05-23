from data.generator import qh_generator
from data.config import Config
conf = Config()

if __name__ == '__main__':
    train_file = "data/train.txt"
    test_file = "data/test.txt"
    test_file_var = "data/test_var.txt"
    qh_generator(conf.get_train_data_size(), train_file, conf.get_input_size())
    qh_generator(conf.get_test_data_size(), test_file, conf.get_input_size())
    qh_generator(conf.get_test_data_size(), test_file_var, conf.var_input_size)