import numpy as np
import matplotlib.pyplot as plt
import math as m
from numpy.lib import scimath
import time

def f(x):
    return np.sin(x) + np.cos(x) + 1
def f1(x):
    return np.cos(x) - np.sin(x)
def f2(x):
    return -np.sin(x) - np.cos(x)

# Vẽ đồ thị
x = np.linspace(3,3.5,100)
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
distance = [3,3.5]

#   Xác định điểm x_0
def check_x_0(distance):
    if f(distance[0])*f2(distance[0]) >0:
        x0 = distance[0]
    else:
        x0 = distance[1]
    return x0

def check_Max_f2p(distance):
    if np.abs(f2(distance[1])) > np.abs(f2(distance[0])):
        M2 = np.abs(f2(distance[1]))
    else:
        M2 = np.abs(f2(distance[0]))
    return M2

def check_Min_f1p(distance):
    if np.abs(f1(distance[1])) > np.abs(f1(distance[0])):
        m1 = np.abs(f1(distance[0]))
    else:
        m1 = np.abs(f1(distance[1]))
    return m1

x0 = check_x_0(distance)
M2 = check_Max_f2p(distance)
m1 = check_Min_f1p(distance)
# print(x0)
# print(M2)
# print(m1)
def main(x0,M2,m1, epsilon):
    x1 = x0 - f(x0)/f1(x0)
    n = 0
    print("n = {}, x_n+1 = {}, x_n = {}".format(n,x1,x0))
    while (M2/(2*m1))*((x1-x0)**2) > epsilon:
        x0 = x1
        x1 = x0 - f(x0)/f1(x0)
        n += 1
        print("n = {}, x_n+1 = {}, x_n = {}".format(n,x1,x0))
    print("Nghiệm gần đúng là: {}".format(x1))

main(x0,M2,m1, epsilon)