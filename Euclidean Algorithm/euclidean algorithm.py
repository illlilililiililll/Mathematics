# 유클리드 호제법(Euclidean Algorithm)

# 최대공약수
# while문
def GCD(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a
        
# 최소공배수
def LCM(a, b):
    return a*b//GCD(a, b)

if __name__ == "__main__":
    a, b = map(int, input().split())

    print("GCD:", GCD(a, b))
    print("LCM:", LCM(a, b))