import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.lib import scimath
import timeit

def f(x):
    return x**3 - 0.2*(x**2) - 0.2*x - 1.2
def f1(x,n):
    return 3*(x**2) - 0.4*x - 0.2
def f2(x,n):
    return 6*x - 0.4

# Vẽ đồ thị
x = np.linspace(1,1.5,100)
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
#   khoảng phân ly và sai số
kpl = [1,1.5]
epsilon = 0.003
c = (kpl[0] + kpl[1])/2
# Xét tính đơn điệu tăng, giảm của f`(x)

if (f1(c) > 0) and (f(kpl[1])*f2(kpl[1])>0):
    x0 = kpl[1]
if (f1(c) < 0) and (f(kpl[0])*f2(kpl[0])>0):
    x0 = kpl[0]






