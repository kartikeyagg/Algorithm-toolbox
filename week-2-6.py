#python3
def fibono(n):
    a = [0,1]
    if n<=2:
        return n
    temp1 = 1
    for i in range(n-1):
        temp = a[0]
        a[0] = a[1]
        a[1] = (a[1] + temp)%10
        temp1 = (temp1+a[1])%10
    return temp1%10

if __name__ == '__main__':
    num = int(input())
    print(fibono(num))