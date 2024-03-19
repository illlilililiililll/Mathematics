import numpy as np
import matplotlib.pyplot as plt

# def f(x):
#     return x*np.sin(x**2)+1

# def df(x):
#     return np.sin(x**2) + 2*(x**2) * np.cos(x**2)

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def df(x):
    return 3*x**2 - 12*x + 11

x_values = np.linspace(-1, 7, 400)
y_values = f(x_values)

initial_x =5
learning_rate = 0.005
momentum_coefficient = 0.8
num_iterations = 300

data = []

fig, axes = plt.subplots(1, 3, figsize=(12, 5))

def gradient_descent(df, initial_x, learning_rate, num_iterations):
    x = initial_x
    x_history = [x]
    for _ in range(num_iterations):
        gradient = df(x)
        x -= learning_rate * gradient
        x_history.append(x)
    return x_history

x_history = gradient_descent(df, initial_x, learning_rate, num_iterations)
data.append(['Gradient Descent', round(f(x_history[-1]), 4), round(df(x_history[-1]), 4)])

axes[0].plot(x_values, y_values, c='black')
axes[0].scatter(x_history[:-1], [f(x) for x in x_history[:-1]], c='blue', alpha=[i/(len(x_history)-1) for i in range(len(x_history)-1)])
axes[0].scatter(x_history[-1], f(x_history[-1]), c='red')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].set_title('Gradient Descent')

def momentum_gradient_descent(df, initial_x, learning_rate, momentum_coefficient, num_iterations):
    x = initial_x
    velocity = 0
    x_history = [x]
    for _ in range(num_iterations):
        gradient = df(x)
        velocity = momentum_coefficient * velocity - learning_rate * gradient
        x += velocity
        x_history.append(x)
    return x_history

x_history = momentum_gradient_descent(df, initial_x, learning_rate, momentum_coefficient, num_iterations)
data.append(['Momentum Gradient Descent', round(f(x_history[-1]), 4), round(df(x_history[-1]), 4)])

axes[1].plot(x_values, y_values, c='black')
axes[1].scatter(x_history[:-1], [f(x) for x in x_history[:-1]], c='blue', alpha=[i/(len(x_history)-1) for i in range(len(x_history)-1)])
axes[1].scatter(x_history[-1], f(x_history[-1]), c='red')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].set_title('Momentum Gradient Descent')

def adaptive_gradient_descent(df, initial_x, learning_rate, num_iterations, epsilon=1e-8):
    x = initial_x
    x_history = [x]
    h = 0
    for _ in range(num_iterations):
        grad = df(x)
        h += grad**2
        x -= learning_rate * grad / (np.sqrt(h) + epsilon)
        x_history.append(x)

    return x_history

x_history = adaptive_gradient_descent(df, initial_x, learning_rate, num_iterations)
data.append(['Adaptive Gradient Descent', round(f(x_history[-1]), 4), round(df(x_history[-1]), 4)])

axes[2].plot(x_values, y_values, c='black')
axes[2].scatter(x_history[:-1], [f(x) for x in x_history[:-1]], c='blue', alpha=[i/(len(x_history)-1) for i in range(len(x_history)-1)])
axes[2].scatter(x_history[-1], f(x_history[-1]), c='red')
axes[2].set_xlabel('x')
axes[2].set_ylabel('y')
axes[2].set_title('Adaptive Gradient Descent')

plt.suptitle('$y = xsin(x^2)+1$', fontsize=13)
plt.show()

data.sort(key=lambda x: x[1])

for i in range(len(data)):
    if data[i][0] == 'Gradient Descent':
        print(f'{i+1}. {data[i][0]}\t\tmin: {data[i][1]}\tderivative: {data[i][2]}')
        continue
    print(f'{i+1}. {data[i][0]}\tmin: {data[i][1]}\tderivative: {data[i][2]}')