import numpy as np
import matplotlib.pyplot as plt
import math as m
from numpy.lib import scimath
import time

def f(x):
    return x**3 + 2*x - 11
def f1(x):
    return 3*(x**2) + 2
def f2(x):
    return 6*x

# Vẽ đồ thị
x = np.linspace(1.9,2,100)
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
epsilon = 1e-6 # Sai số của bài toán
#distance = [9,10] # Chọn khoảng cách ly nghiệm cho bài toán '''
distance = [1.9,2]
c = (distance[0]+distance[1])/2
#XÉT TÍNH ĐƠN ĐIỆU TĂNG GIẢM CỦA f`(x) (Chỉ đúng với TH f`(x) != 0 và đơn điệu trên KPL)
if f1(c) > 0:
    M = f1(distance[1])
    m = f1(distance[0])
    d = distance[1]
    x0 = distance[0]
if f1(c) < 0:
    M = f1(distance[0])
    m = f1(distance[1])
    d = distance[0]
    x0 = distance[1]

def main(x0,d,M,m, epsilon):
    x1 = x0 - (f(x0)*(d-x0))/(f(d)-f(x0))
    x_m = x1
    x_n = x0
    n = 0
    print("n = {}, x_n+1 = {}, x_n = {}".format(n,x_m,x_n))
    while np.abs(x_m-x_n) > (epsilon*m)/(M-m):
        x_n = x_m
        x_m = x_m - (f(x_m)*(d-x_m))/(f(d)-f(x_m))
        n += 1
        print("n = {}, x_n+1 = {}, x_n = {}".format(n,x_m,x_n))
    print("Nghiệm gần đúng là: {}".format(x_m))

main(x0,d,M,m, epsilon)

