import pickle as pk
import random

# size for training data
train_size = 10000

# size for testing data
test_size = 1000

# size for input of RNN
input_size = 10

# range of random integer
up_bound = 10
low_bound = -10

train_file = "train.txt"
test_file = "test.txt"


# DP solution
def mss(arr):
    dp = []
    dp.append(arr[0])
    result = arr[0]
    for i in range(1, input_size):
        curr = max(dp[i - 1] + arr[i], arr[i])
        dp.append(curr)
        result = max(result, curr)
    return result


def input_generator():
    arr = []
    for i in range(input_size):
        arr.append(random.randint(low_bound, up_bound))
    return arr


def mss_generator(size, file):
    input_data = []
    output_data = []
    for i in range(size):
        arr = input_generator()
        input_data.append(arr)
        result = mss(arr)
        output_data.append(result)
    with open(file, "wb") as f:
        pk.dump((input_data, output_data), f)


# brute force solution
def check_sum(arr, out):
    maximum = arr[0]
    for i in range(len(arr)):
        curr = 0
        for j in range(i, len(arr)):
            curr += arr[j]
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
    mss_generator(train_size, train_file)
    mss_generator(test_size, test_file)
    # check(train_file)
