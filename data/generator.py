import pickle as pk
import random

from data.config import Config

conf = Config()

low_bound = conf.get_low_bound()
up_bound = conf.get_up_bound()
eos = conf.get_eos()


# DP solution
def mss(arr):
    dp = []
    dp.append(arr[0])
    result = arr[0]
    for i in range(1, len(arr)):
        curr = max(dp[i - 1] + arr[i], arr[i])
        dp.append(curr)
        result = max(result, curr)
    return [result]


def input_generator(length):
    arr = []
    elements = random.randint(1, length)
    for i in range(elements):
        arr.append(random.randint(low_bound, up_bound))
    return arr


def fill_arr(arr, length):
    while len(arr) < length:
        arr.append(eos)
    arr.append(eos)


def mss_generator(data_size, file, data_length):
    input_data = []
    output_data = []
    for i in range(data_size):
        arr = input_generator(data_length)
        result = mss(arr)
        fill_arr(arr, data_length)
        fill_arr(result, data_length)
        input_data.append(arr)
        output_data.append(result)
    with open(file, "wb") as f:
        pk.dump((input_data, output_data), f)


# brute force solution
def check_sum(arr, out, index):
    seq = []
    for num in arr:
        if num == eos:
            break
        seq.append(num)
    res = out[0]
    maximum = seq[0]
    for i in range(len(seq)):
        curr = 0
        for j in range(i, len(seq)):
            curr += seq[j]
            if curr > maximum:
                maximum = curr
    if res != maximum:
        print("false at index {}".format(index))


def check(file):
    with open(file, "rb") as f:
        (x, y) = pk.load(f)
    length = len(x)
    for i in range(length):
        # check_sum(x[i], y[i], i)
        print("{}, {}".format(x[i], y[i]))


if __name__ == '__main__':
    train_file = "train.txt"
    test_file = "test.txt"
    test_file_var = "test_var.txt"
    mss_generator(10000, train_file, 5)
    mss_generator(1000, test_file, 5)
    mss_generator(1000, test_file_var, 10)
    check(train_file)
    # check(test_file)
    # check(test_file_var)
