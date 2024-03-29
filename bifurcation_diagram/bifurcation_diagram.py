import numpy as np
import matplotlib.pyplot as plt
import singleBifurcation

def bifurcate(seed:float, n_skip:int, n_iter:int, step:float=0.0001, r_min:float=0.0):
    X = []
    Y = []
    _range = np.linspace(r_min, 4, int(1/step))
    for x in _range:
        y = seed
        for i in range(n_skip+n_iter+1):
            if i >= n_skip:
                X.append(x)
                Y.append(y)
            y = singleBifurcation.logistic(x, y)
   
    plt.plot(X, Y, ls='', marker=',', color='black')
    plt.ylim(0, 1)
    plt.xlim(r_min, 4)
    plt.show()

if __name__ == "__main__":
    bifurcate(0.2, 100, 10, r_min=1)