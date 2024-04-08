import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*np.sin(x**2)+1

def df(x):
    return np.sin(x**2) + 2*(x**2) * np.cos(x**2)

x_values = np.linspace(-2.5, 2.5, 400)
y_values = f(x_values)

initial_x = 1
learning_rate = 0.01
momentum_coefficient = 0.92
num_iterations = 300

def gradient_descent(df, initial_x, learning_rate, num_iterations):
    x = initial_x
    x_history = [x]
    for _ in range(num_iterations):
        gradient = df(x)
        x -= learning_rate * gradient
        x_history.append(x)
    return x_history

x_history = gradient_descent(df, initial_x, learning_rate, num_iterations)
print(f'min : {f(x_history[-1]):.4f}\tderivative: {df(x_history[-1]):.4f}')

plt.plot(x_values, y_values, c='black')
plt.scatter(x_history[:-1], [f(x) for x in x_history[:-1]], c='blue', alpha=[i/(len(x_history)-1) for i in range(len(x_history)-1)])
plt.scatter(x_history[-1], f(x_history[-1]), c='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradient Descent')
plt.show()