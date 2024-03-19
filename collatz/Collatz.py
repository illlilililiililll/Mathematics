import matplotlib.pyplot as plt
from collections import deque

def collatz(i):
    history = deque()
    count = 0
    history.append(i)
    while i != 1:
        if i % 2 == 1:
            i = i*3 + 1
        else:
            i //= 2
        history.append(i)
        count += 1
    
    return history, count

for i in range(1, 100):
    history, count = collatz(i)
    plt.plot(range(count+1), history, alpha=0.5)
    print(f"#{i}")

plt.savefig("C:/Users/renew/Desktop/py/hana/math/collatz/Collatz.png")
plt.show(block=True)