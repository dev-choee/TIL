# 2884 ěë ěęł
def sol2884():
    h,m=map(int,input().split())

    if m-45<0:
        m = 60+m-45
        if h==0:
            h=23
        else:
            h=h-1
    else:
        m = m-45 
        
    print(h,m) 