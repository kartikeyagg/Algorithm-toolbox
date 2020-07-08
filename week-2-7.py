#python3


def fibono(nm,n):

    a = [0,1]
    if n<=1:
        return n
    temp1 = 1
    temp2 = 0
    for i in range(n-1):
        a.append((a[-1]+a[-2])%10)
        a.pop(0)
        temp1 = (temp1 + a[-1])
        if i == nm-3:
            temp2 = temp1


    return ((temp1-temp2)%10)


if __name__ == '__main__':
    num,n = (int(i) for i in input().split())
    print(fibono(num,n))