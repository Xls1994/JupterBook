# -*- coding: utf-8 -*-
'''
author:yangyl
plot the tanh and sigmoid functions
'''
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1./(1+np.exp(-x))
def plots():
    x =np.linspace(-10,10,101)
    y =np.tanh(x)+sigmoid(x)
    tanh_y =np.tanh(x)
    sigmoid_y =sigmoid(x)
    zero =np.zeros((101,))
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r')
    ax.plot(x, sigmoid_y, 'k--', lw=4)
    ax.plot(x,tanh_y,'b-')
    ax.plot(x,zero,'g')
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    plt.show()

if __name__ == '__main__':
    plots()