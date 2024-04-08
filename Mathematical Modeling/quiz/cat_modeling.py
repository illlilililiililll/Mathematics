from random import randint
import matplotlib.pyplot as plt

data = []

for _ in range(1, 3001):
    history = []
    for i in range(_):
        mouse = 4
        count = 0
        while mouse not in [1, 7]:
            n = randint(0, 1)
            if n == 0:
                mouse -= 1
            else:
                mouse += 1
            count += 1
        history.append(count)
    data.append(sum(history)/len(history))
    print(f"{_}회 시행: {sum(history)/len(history)}")

print(f'{round(sum(data)/len(data), 4)}시간')
plt.plot(data)
plt.show()