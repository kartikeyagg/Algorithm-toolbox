#python3
def fibono(n):
    a = [0,1]
    if n<=1:
        return n
    for i in range(n-1):
        a.append((a[-1]+a[-2])%10)
        '''temp = a[0]
        a[0] = a[1]
        a[1] = a[1] + temp'''
        a.pop(0)
    return (a[-1])

if __name__ == '__main__':
    num = int(input())
    print(fibono(num))