import math
import numpy as np
import matplotlib.pyplot as plt
# Hàm f(x) = x^3 + x - 1000
def f(x):
    #return x**3 + x - 1000
    return x**5 - x - 1
    
# Hàm g(x) = (1000-x)^(1/3)
def g(x):
    #return (1000-x)**(1/3)
    return (x+1)**(1/5)

# Hàm gDeri = (-1)^n x g'(x) 
def gDeri(x,n):     #đạo hàm của g(x)
    #return ((-1)**n)*(-1/3*(1000-x)**(-2/3))
    return 1/5*((x+1)**(-4/5))

# Đạo hàm cho hàm gDeri
def deri(x,n):
    dy = gDeri(x+10e-9,n)-gDeri(x-10e-9,n)
    dx = 2*10e-9
    return dy/dx

# Vẽ đồ thị
x = np.linspace(5,12,100)
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

# INIT
epsilon = 1e-6 # Sai số của bài toán
#distance = [9,10] # Chọn khoảng cách ly nghiệm cho bài toán '''
distance = [1,2]
start = distance[0] 
end = distance[1] 


# Thuật toán Gradient dencents 
def gd(distance, n):
    x = [distance[0]]
    for i in range(100):
        x_new = x[-1] - 0.1*deri(x[-1],n)
        if abs(deri(x_new,n)) < 1e-3:
           break
        x.append(x_new)
    return x[-1] 

# Tìm cực tiểu
def minima(distance, value):
    n = 0 
    a = gd(distance, n)
    distance[0] = a + 10e-3
    b = gDeri(a, n)
    if a >= start and a <= end:
        value.append(b)
    return distance, value

# Tìm cực đại
def maxima(distance, value):
    n = 1 
    a = gd(distance, n)
    distance[0] = a + 10e-3
    b = gDeri(a, 0)
    if a >= start and a <= end:
        value.append(b)
    return distance, value

# Tìm tất cả cực trị trong khoảng phân ly nghiệm
def ext(distance, value):
    if distance[0] >= distance[1]:
        return value
    else:
        if deri(distance[0], 0) < 0:
            distance, value = minima(distance, value)
        else:
            distance, value = maxima(distance, value)
        return ext(distance, value)

# Tìm max của  |g(x)'| trong khoảng phân ly nghiệm
def maxAbsolute():
    value =[]
    value.append(gDeri(distance[0],0))
    value.append(gDeri(distance[1],0))

    value = ext(distance, value)
    value.sort()

    # Công thức nhanh tính giá trị max của |g(x)'|
    value_max = (abs(value[0]+value[-1]) + abs(value[0]-value[-1])) / 2
     
    return value_max

q = maxAbsolute()

# Phương pháp lặp đơn với sai số hậu nghiệm
def repeatMethod1(x0, epsilon):
    if q >= 1:
        print("Điều kiện hội tụ không thỏa mãn")
    else:
        epsilon_0 = ((1 - q)*epsilon) / q
        loop = 1
        while(1):
            x1 = g(x0)
            print("loop = {}, x1 = {}, x0 = {}, f(x)= {}".format(loop,x1,x0,f(x1)))
            if abs(x1-x0) < epsilon_0:
                break
            x0 = x1
            loop = loop + 1
        print("Nghiệm gần đúng của phương trình là: {}".format(x1))

# Thực hiện chương trình
repeatMethod1(start, epsilon)