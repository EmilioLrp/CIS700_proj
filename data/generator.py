import numpy as np
import random
import json
from typing import List
import pickle as pk
from data.config import Config


conf = Config()

low_bound = conf.get_low_bound()
up_bound = conf.get_up_bound()
eos = conf.get_eos()


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # if the list of merged intervals is empty or if the current
        # interval does not overlap with the previous, simply append it.
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


def input_generator(length):
    intervals = []
    elements = random.randint(1, int(length/2))
    inter = 5  # difference between start and end
    for i in range(elements):
        start = random.randint(low_bound, up_bound)
        end = start + random.randint(1, inter)
        intervals.append([start, end])
    return intervals


def fill_arr(arr, length):
    while len(arr) < length:
        arr.append(eos)
    arr.append(eos)


def qh_generator(data_size, file, data_length):
    inputs = []
    outputs = []
    for x in range(data_size):
        intervals = input_generator(data_length)

        output = merge(intervals)
        flatten = [i for k in intervals for i in k]
        fill_arr(flatten, data_length)
        inputs.append(flatten)
        flatten2 = [i for k in output for i in k]
        fill_arr(flatten2, data_length)
        outputs.append(flatten2)
    with open(file, "wb") as f:
        pk.dump((inputs, outputs), f)


def check(file):
    with open(file, "rb") as f:
        (x, y) = pk.load(f)
    length = len(x)
    print(length)


if __name__ == '__main__':
    train_file = "train.txt"
    test_file = "test.txt"
    test_file_var = "test_var.txt"
    qh_generator(conf.get_train_data_size(), train_file, conf.get_input_size())
    qh_generator(conf.get_test_data_size(), test_file, conf.get_input_size())
    qh_generator(conf.get_test_data_size(), test_file_var, conf.var_input_size)
    check("test_var.txt")
