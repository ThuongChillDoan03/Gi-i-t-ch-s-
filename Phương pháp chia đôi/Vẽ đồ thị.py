import numpy as np
import matplotlib.pyplot as plt

#Hàm f(x) - sửa một hàm bất kì mà bạn muốn
def f(x):
    return np.log(3 * x) + pow(2, x) - 2 * x -2

# Vẽ đồ thị hàm số
plt.xlabel("Giá trị x biến thiên")
plt.ylabel("Giá trị y biến thiên")
plt.title("Đồ thị hàm số của phương trình f(x) ")
x = np.linspace(0,3.5 , 1000)
plt.plot(x, f(x))
plt.plot(0, 0, '+')
plt.plot(0, )
plt.grid()
plt.show()