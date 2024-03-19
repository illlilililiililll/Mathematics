# 유클리드 호제법(Euclidean Algorithm)

# 최대공약수
# 재귀함수
def GCD(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

# 최소공배수
def LCM(a, b):
    return a*b//GCD(a, b)

if __name__ == "__main__":
    a, b = map(int, input().split())

    print("GCD:", GCD(a, b))
    print("LCM:", LCM(a, b))