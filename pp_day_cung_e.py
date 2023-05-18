import numpy as np
import matplotlib.pyplot as plt
import math as m
from numpy.lib import scimath
import time

def f(x):
    return np.log(x) - 1
def f1(x):
    return 1/x
def f2(x):
    return -1/(x**2)

# Vẽ đồ thị
x = np.linspace(2,4,100)
y = f(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,y, 'r')
plt.show()

# INIT  TỰ THAY ĐỔI Ở ĐÂY
epsilon = 1e-9 # Sai số của bài toán
#distance = [9,10] # Chọn khoảng cách ly nghiệm cho bài toán '''
distance = [2,4]
c = (distance[0]+distance[1])/2
#XÉT TÍNH ĐƠN ĐIỆU TĂNG GIẢM CỦA f`(x) (Chỉ đúng với TH f`(x) != 0 và đơn điệu trên KPL)

def check_d(distance):
    st = distance[0]
    end = distance[1]
    x2 = (st*f(end)-end*f(st))/(f(end)-f(st))
    if f(x2)*f(st) > 0:
        x0 = st
        d = end
    else:
        x0 = end
        d = st 
    return x0, d

def checkMaxMin(distance):
    if np.abs(f1(distance[1]))>np.abs(f1(distance[0])):
        M = np.abs(f1(distance[1]))
        m = np.abs(f1(distance[0]))
    else:
        M = np.abs(f1(distance[0]))
        m = np.abs(f1(distance[1]))
    return M,m

x0,d = check_d(distance)
M,m = checkMaxMin(distance)
# print(x0,d)
# print(M,m)
def main(x0,d,M,m, epsilon):
    x1 = x0 - (f(x0)*(d-x0))/(f(d)-f(x0))
    x_m = x1
    x_n = x0
    n = 0
    print("n = {}, x_n+1 = {}, x_n = {}".format(n,x_m,x_n))
    while (np.abs(x_m-x_n)) > (epsilon*m)/(M-m):
        x_n = x_m
        x_m = x_m - (f(x_m)*(d-x_m))/(f(d)-f(x_m))
        n += 1
        print("n = {}, x_n+1 = {}, x_n = {}".format(n,x_m,x_n))
    print("Nghiệm gần đúng là: {}".format(x_m))

main(x0,d,M,m, epsilon)