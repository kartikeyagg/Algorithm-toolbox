#python3
def gcdrec(p, y , z):
    p.sort()
    p[-1] = p[-1]%p[-2]
    if p[-1] != 0:
        gcdrec(p,y,z)
    else :
        print(int((y*z)/p[0]))
if __name__ == '__main__':
    x = (input())
    y,z = (int(i) for i in x.split())
    p=[]
    p.append(y)
    p.append(z)
    gcdrec(p, y, z)

