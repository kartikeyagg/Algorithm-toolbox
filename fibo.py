#python3
def fibono(n):
    a = [0,1]
    if n<=1:
        return n
    for i in range(n-2):
        a.append(a[-1]+a[-2])
    return a[-1]

if __name__ == '__main__':
    num = int(input())
    print(fibono(num))