def EEA(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = EEA(b, a%b)
        return d, y, x - y*(a//b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(EEA(a, b))