import matplotlib.pyplot as plt
import numpy as np
import pickle
'''
# Example
train_loss = [0.3, 0.32, 0.432, 0.43, 0.6, 0.1, 0.5,0.7,0.6,0.9,0.3,0.5,0.2,0.8]
test_loss = [0.8, 0.3, 0.832, 0.13, 0.4, 0.1, 0.3,0.8]
test_loss2 = [0.6,0.9,0.3,0.5,0.2,0.8,0.3,0.1]


with open('train_loss.txt','r') as f:
    train_loss = eval(f.read())

with open('test_loss.txt','r') as f:
    test_loss = eval(f.read())

with open('test_loss2.txt','r') as f:
    test_loss2 = eval(f.read())
'''

with open('train_loss.txt', 'rb') as f:
    loss = pickle.load(f)
    train_loss = loss[0]
    #train_loss = loss[1]

with open('test_loss.txt', 'rb') as f:
    test_loss = pickle.load(f)

with open('test_loss2.txt', 'rb') as f:
    test_loss2 = pickle.load(f)

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.plot(np.arange(1, len(train_loss)+1, 1), train_loss, label = 'train', color = 'red')


ax1.set_xlabel('iterations')
ax1.set_ylabel('loss')


ax2 = plt.twiny()
ax2.plot(np.arange(1, len(test_loss)+1, 1), test_loss, label = 'test', color = 'blue')
ax2.plot(np.arange(1, len(test_loss2)+1, 1), test_loss2, label = 'test2', color = 'green')
ax2.set_xlabel('test')

fig.legend()

plt.show()
