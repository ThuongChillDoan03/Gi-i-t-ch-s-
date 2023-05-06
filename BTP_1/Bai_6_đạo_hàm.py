# Tính đạo hàm tại x0 của 1 hàm cho trước
#   f`(x) = lim(x--->x0)(f(x)-f(x0))/(x-x0) sử dụng định nghĩa của đạo hàm

import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.lib import scimath

def f(x):
    return np.log(x) + x**3 - 12

# # Vẽ đồ thị #(Nếu cần thì dùng sau)
# x = np.linspace(1.9,2,100)
# y = f(x)

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')

# plt.plot(x,y, 'r')
# plt.show()

x0 = float(input("Tính đạo hàm của f(x) tại điểm x0 là: "))
epsilon = float(input("Sai số của x tiến tới điểm x0: "))       #nên để <= 10^-6
def derivative_fx(x0, epsilon):
    f1x = (f(x0+epsilon)-f(x0))/(epsilon)
    print("Đạo hàm của f(x) tại điểm x0 là: ", f1x)

derivative_fx(x0, epsilon)
