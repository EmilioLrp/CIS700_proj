import pickle as pk
import math
import random
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(BASE_DIR)

from data.config import Config

conf = Config()

low_bound = conf.get_low_bound()
up_bound = conf.get_up_bound()
eos = conf.get_eos()

def check_odd_even(arr):
    result = []
    for i in range(len(arr)):
        if (int(arr[i]) % 2) == 0:
            # 1002 represents Even
            result.append(1002)
        else:
            # 1001 represents Odd
            result.append(1001)
    return result

def arr_generator(length):
    arr = []
    elements = random.randint(1, length)
    for i in range(elements):
        arr.append(random.randint(low_bound, up_bound))
    return arr

def fill_arr(arr, length):
    while len(arr) < length:
        arr.append(eos)
    arr.append(eos)

def data_generator(problem_size, data_file, data_length):
    input_data = []
    output_data = []
    for i in range(problem_size):
        arr = arr_generator(data_length)
        result = check_odd_even(arr)
        fill_arr(arr, data_length)
        fill_arr(result, data_length)
        input_data.append(arr)
        output_data.append(result)
    with open(data_file, "wb") as f:
        pk.dump((input_data, output_data), f)

if __name__ == '__main__':
    train_file = "train.txt"
    test_file = "test.txt"
    test2_file = "test2.txt"
    data_generator(conf.get_train_data_size(), train_file, conf.get_input_size())
    data_generator(conf.get_test_data_size(), test_file, conf.get_input_size())
    data_generator(conf.get_test_data_size(), test2_file, conf.var_input_size)
    


    

