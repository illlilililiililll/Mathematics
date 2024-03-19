import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import sympy as sp

# user-input
X = np.array([])
y = np.array([])

while 1:
    n = input().strip()
    if n == '!':
        break
    try:
        a, b = map(float, n.split())
        X = np.append(X, a)
        y = np.append(y, b)
    except ValueError:
        print('\nInvalid input')
        print('the format is "x y"')
        continue

# 데이터 형태 변경
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# 다항 회귀 모델 설정 및 학습
poly_features = PolynomialFeatures(degree=len(X)-1, include_bias=False)
X_poly = poly_features.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)

# 모델의 계수 및 절편 가져오기
coefs = model.coef_.flatten()
intercept = model.intercept_[0]

# f(x) 함수 정의
def f(x, coefs, intercept):
    return intercept + sum(coef * np.power(x, power) for coef, power in zip(coefs, range(1, len(coefs) + 1)))

# 새로운 데이터에 대한 예측
x_new = np.linspace(-100, 100, 100)
y_new = f(x_new, coefs, intercept)

x = sp.symbols('x')

# 다항 회귀 모델의 식 생성
polynomial_expr = round(intercept, 4) + sum(round(coef, 4) * x**power for coef, power in zip(coefs, range(1, len(coefs) + 1)))
highest_coef = coefs[-1]
new_poly = round(intercept/highest_coef, 4) + sum(round(coef/highest_coef, 4) * x**power for coef, power in zip(coefs, range(1, len(coefs) + 1)))
print('y =', polynomial_expr)

def newton_raphson(func_str, x0, tol=1e-5, max_iter=1000):

    x = sp.symbols('x')
    f = sp.sympify(func_str)
    df = sp.diff(f, x)

    # Convert symbolic functions to numerical functions
    f_lambda = sp.lambdify(x, f, "numpy")
    df_lambda = sp.lambdify(x, df, "numpy")

    # Actual Newton-Raphson iteration
    for _ in range(max_iter):
        x_new = x0 - f_lambda(x0) / df_lambda(x0)

        # Check for convergence
        if abs(x_new - x0) < tol:
            return x_new

        x0 = x_new

    raise ValueError("Failed to converge after {} iterations.".format(max_iter))

# Example usage:

root = newton_raphson(str(new_poly), float(len(X)-1))
print("함수의 근:", root)

def visualize_function(func, X, y, x_range=(-50, 50), num_points=1000):
    x_values = np.linspace(x_range[0], x_range[1], num_points)
    y_values = [func(x) for x in x_values]

    plt.plot(x_values, y_values, label='f(x)')
    plt.xlabel('x-values')
    plt.ylabel('y-values')
    plt.title('Visualization of Function')
    plt.legend()
    plt.grid(True)
    plt.scatter(X, y)
    plt.plot(root, 0, marker="o")
    plt.xlim([-10,10 ])
    plt.ylim([-10, 10])
    plt.show()

if __name__ == "__main__":
    x = sp.symbols('x')
    # Example: Define your polynomial expression here

    # Convert the symbolic expression to a numerical function
    polynomial_func = sp.lambdify(x, polynomial_expr, "numpy")

    visualize_function(polynomial_func, X, y)