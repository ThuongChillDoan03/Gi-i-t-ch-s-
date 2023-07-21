import numpy as np
DCX = 5
SAISO = 10**(-DCX)
def Nghiem(list):
    if len(list)==1:
        return []
    upper = 1 + max(abs(i) for i in list[1:])/abs(list[0])
    CucTri = []
    CucTri.append(-upper)
    CucTri.extend(Nghiem(DaoHam(list)))
    CucTri.append(upper)
    nghiem = []
    for i in range(len(CucTri)-1):
        if f(CucTri[i],list) * f(CucTri[i+1],list) < 0:
            nghiem.append(ChiaDoi(CucTri[i],CucTri[i+1],list))
        elif abs(f(CucTri[i],list)) <= SAISO:
            nghiem.append(CucTri[i])
    if abs(f(CucTri[-1], list)) <= SAISO:
        nghiem.append(CucTri[-1])
    return nghiem

#PHUONG PHAP CHIA DOI VOI KHOANG CACH LY NGHIEM (a;b)
def ChiaDoi(a,b,list):
    mid = (a + b) / 2
    t = f(mid,list)
    i = 0
    while (abs(t) > SAISO and i < 10000):
        if (t * f(a,list) > 0):
            a = mid
        else:
            b = mid
        mid = (a + b) / 2
        t = f(mid,list)
        i += 1
    #print(mid, f(mid, list))
    return round(mid,DCX)

#TINH GIA TRI CUA HAM DA THUC TAI X
def f(x,list):
    n = len(list)
    value = 0
    for i in range(n):
        value += list[i]*(x**(n-i-1))
    return value

#TINH HE SO CUA DA THUC SAU DAO HAM
def DaoHam(list):
    m = len(list)-1
    daoham = []
    for i in range(m):
        daoham.append((m-i)*list[i])
    return daoham