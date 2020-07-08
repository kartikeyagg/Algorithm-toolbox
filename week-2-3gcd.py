#python3
def gcdrec(p):
    p.sort()
    p[-1] = p[-1]%p[-2]
    if p[-1] != 0:
        gcdrec(p)
    else :
        print(p[0])
if __name__ == '__main__':
    x = (input())
    y,z = (int(i) for i in x.split())
    p=[]
    p.append(y)
    p.append(z)
    gcdrec(p)

