# python3
def fibono(n,num):
    a = [0, 1]
    if n <= 1:
        return n
    for i in range(n - 2):
        a.append((a[-1] + a[-2]) % num)
        a.pop(0)
        '''temp = a[0]
        a[0] = a[1]
        a[1] = (a[1] + temp)%num'''
    return ((a[-1] + a[-2]))%num


if __name__ == '__main__':
    n, num = (int(i) for i in input().split())
    print(fibono(n, num))
