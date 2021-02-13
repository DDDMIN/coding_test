#8-2 피보나치 수열 소스코드(Memorization)
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    #계산한적이 있는 문제면 저장된 값 그대로 반환
    if d[x] != 0:
        return d[x]
    #계산한 적이 없으면 피보나치 수열 계산
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))


#8-2 피보나치 수열 소스코드(Memorization)
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    #계산한적이 있는 문제면 저장된 값 그대로 반환
    if d[x] != 0:
        return d[x]
    #계산한 적이 없으면 피보나치 수열 계산
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

