import pickle as pk
import random

from data.config import Config
conf = Config()

low_bound = conf.get_low_bound()
up_bound = conf.get_up_bound()
eos = conf.get_eos()

def mss(arr):
    '''pal = []
    for i in arr:
        if i != eos:
            pal.append(i)
    result = str(pal) == str(pal)[::-1]'''

    result = []
    for i in arr:
        result.append(str(i) == str(i)[::-1])
    return result

def randomint_generator(length):
    arr = []
    for i in range(length):
        arr.append(random.randint(low_bound, up_bound))
    return arr

def palindrome_generator(length):
    arr = []
    for i in range(length):
        a = list(str(random.randint(low_bound, up_bound)))
        i = 0
        j = len(a)
        while j > (len(a)/2):
            a[j-1] = a[i]
            j -= 1
            i += 1
        a = int(''.join(a))
        arr.append(a)

    return arr

def fill_arr(arr, length):
    while len(arr) < length:
        arr.append(eos)
    arr.append(eos)

def mss_generator(data_size, file, data_length):
    input_data = []
    output_data = []
    for i in range(int(0.65 * data_size)):
        arr = randomint_generator(data_length)
        result = mss(arr)
        fill_arr(arr, data_length)
        fill_arr(result, data_length)
        input_data.append(arr)
        output_data.append(result)
    for i in range(int(0.35 * data_size)):
        arr = palindrome_generator(data_length)
        result = mss(arr)
        fill_arr(arr, data_length)
        fill_arr(result, data_length)
        input_data.append(arr)
        output_data.append(result)
    with open(file, "wb") as f:
        pk.dump((input_data, output_data), f)

def run():
    train_file = "data/train.txt"
    test_file = "data/test.txt"
    test_file_var = "data/test_var.txt"
    mss_generator(conf.get_train_data_size(), train_file, conf.get_input_size())
    mss_generator(conf.get_test_data_size(), test_file, conf.get_input_size())
    mss_generator(conf.get_test_data_size(), test_file_var, conf.var_input_size)

if __name__ == '__main__':
    train_file = "train.txt"
    test_file = "test.txt"
    test_file_var = "test_var.txt"
    mss_generator(conf.get_train_data_size(), train_file, conf.get_input_size())
    mss_generator(conf.get_test_data_size(), test_file, conf.get_input_size())
    mss_generator(conf.get_test_data_size(), test_file_var, conf.var_input_size)