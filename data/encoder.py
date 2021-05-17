import numpy as np
import torch

def encoder(inputlist, u_bound, l_bound, threshold, length):

    u_mod = u_bound + threshold
    l_mod = l_bound + threshold
    eos = u_mod + 1
    #u_bi = bin(u_mod).replace('0b', '')
    #l_bi = bin(l_mod).replace('0b', '')
    eos_bi = bin(eos).replace('0b', '')
    lmax = len(eos_bi)

    bilist = []
    for n in inputlist:
        n_bi = bin(n).replace('0b', '')
        bilist.append(n_bi)
    for i in range(length - len(inputlist)):
        bilist.append(eos_bi)

    nbilist = []
    for n in bilist:
        if len(n) < lmax:
            d = lmax - len(n)
            while d > 0:
                n = '0' + n
                d -= 1
            p = n
            nbilist.append(p)
        else:
            nbilist.append(n)
    #print(nbilist)

    m1 = []
    for i in range(len(nbilist)):
        l1 = []
        for j in range(len(nbilist[i])):
            l1.append(nbilist[i][j])
        l1 = list(map(int, l1))
        m1.append(l1)

    return torch.from_numpy(np.transpose(m1))

