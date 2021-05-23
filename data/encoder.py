import torch


def encoder(num, threshold, length):
    # shift the range of number
    # u_mod = u_bound + threshold
    # l_mod = l_bound + threshold

    n = num + threshold
    result = []
    for i in range(length):
        remainder = n % 2
        result.append(remainder)
        n = n // 2

    return torch.tensor(result)


if __name__ == '__main__':
    low = -11
    up = 100
    shift = -low
    length = 7

    result = encoder(100, shift, length)

    check = 0
    for i in range(len(result)):
        if result[i] == 1:
            check += 2 ** i

    print(check - shift)
