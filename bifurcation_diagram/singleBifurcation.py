import numpy as np
import matplotlib.pyplot as plt

def logistic(r:float, x:float):
    return r*x*(1-x)

def graph(r:float, x0:float, n:int):
    x = np.zeros(n+1)
    x[0] = x0
    for i in range(n):
        x[i+1] = logistic(r, x[i])
    plt.plot([i for i in range(1, n+1)], x[1:], alpha=0.25)
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.title(f'Logistic Map')

if __name__ == '__main__':
    for i in np.arange(3.9, 3.91, 0.01):
        graph(i, 0.5, 100)
    plt.show()