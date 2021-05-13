import pickle as pk
import random

# range of random integer
up_bound = 32
low_bound = -32

soc = "SOC"


# DP solution
def mss(arr):
    dp = []
    dp.append(arr[0])
    result = arr[0]
    for i in range(1, len(arr)):
        curr = max(dp[i - 1] + arr[i], arr[i])
        dp.append(curr)
        result = max(result, curr)
    return result


def input_generator(length):
    arr = []
    elements = random.randint(1, length)
    for i in range(elements):
        arr.append(random.randint(low_bound, up_bound))
    return arr


def fill_arr(arr, length):
    while len(arr) < length:
        arr.append(soc)
    arr.append(soc)


def mss_generator(data_size, file, data_length):
    input_data = []
    output_data = []
    for i in range(data_size):
        arr = input_generator(data_length)
        result = mss(arr)
        fill_arr(arr, data_length)
        input_data.append(arr)
        output_data.append(result)
    with open(file, "wb") as f:
        pk.dump((input_data, output_data), f)


# brute force solution
def check_sum(arr, out):
    seq = []
    for num in arr:
        if num == soc:
            break
        seq.append(num)

    maximum = seq[0]
    for i in range(len(seq)):
        curr = 0
        for j in range(i, len(seq)):
            curr += seq[j]
            if curr > maximum:
                maximum = curr
    if out == maximum:
        print(True)
    else:
        print(False)


def check(file):
    with open(file, "rb") as f:
        (x, y) = pk.load(f)
    length = len(x)
    for i in range(length):
        check_sum(x[i], y[i])


if __name__ == '__main__':
    train_file = "train.txt"
    test_file = "test.txt"
    test_file_var = "test_var.txt"
    mss_generator(10000, train_file, 10)
    mss_generator(1000, test_file, 10)
    mss_generator(1000, test_file_var, 20)
