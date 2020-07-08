#python3
def fibono(n):
    a = [0,1]
    if n<=1:
        return n
    for i in range(n):
        a.append(a[-1]+a[-2])
        a.pop(0)
        '''temp = a[0]
        a[0] = a[1]
        a[1] = a[1] + temp'''
    return ((a[1]*a[0])%10)

if __name__ == '__main__':
    num = int(input())
    print(fibono(num))