import math
import numpy as np 
import matplotlib.pyplot as plt

def f1(x):
    return np.cos(x) - np.sin(x)

def f(x):
    return np.sin(x) + np.cos(x) + 1

def f2(x):
    return -np.sin(x) - np.cos(x)

print("Nhập khoảng phân ly!")
a = float(input("Nhập cận nhỏ a: "))
b = float(input("Nhập cận lớn b: "))
x0 = a
eta = 0.1   # eta nên chọn nhỏ để hội tụ tới nghiệm chuẩn hơn

def myGD_CTf1(eta, x0):     #cực tiểu f1(x)
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta*f1(x[-1])
        if (abs(f1(x_new)) < 1e-3) or (abs(f1(x_new)) > 2**128):
            break
        x.append(x_new)
    return (x, it)

def myGD_CĐf1(eta, x0):     #cực đại f1(x)
    x = [x0]
    for it in range(100):
        x_new = x[-1] + eta*f1(x[-1])
        if (abs(f1(x_new)) < 1e-3) or (abs(f1(x_new)) > 2**128):
            break
        x.append(x_new)
    return (x, it)

def myGD_CTf2(eta, x0):     #cực tiểu f2(x)
    xt = [x0]
    for it in range(100):
        x_new = xt[-1] - eta*f2(xt[-1])
        if (abs(f2(x_new)) < 1e-3) or (abs(f2(x_new)) > 2**128):
            break
        xt.append(x_new)
    return (xt, it)

def myGD_CĐf2(eta, x0):     #cực đại f2(x)
    xt = [x0]
    for it in range(100):
        x_new = xt[-1] + eta*f2(xt[-1])
        if (abs(f2(x_new)) < 1e-3) or (abs(f2(x_new)) > 2**128):
            break
        xt.append(x_new)
    return (xt, it)

check = 1
def main_check_condition(check,x0,a,b):
    if f1(x0) > 0:
        (x, it) = myGD_CĐf1(eta, x0)
        test = x[-1]
        if a < test < b:
            check = 0
    else:
        (x, it) = myGD_CTf1(eta, x0)
        test = x[-1]
        if a < test < b:
            check = 0
    
    if f2(x0) > 0:
        (xt, it) = myGD_CĐf2(eta, x0)
        test1 = xt[-1]
        if a < test1 < b:
            check = 0
    else:
        (xt, it) = myGD_CTf2(eta, x0)
        test1 = xt[-1]
        if a < test1 < b:
            check = 0
    return check

check_run = main_check_condition(check,x0,a,b)
if check_run == 0:
    print("Khoảng phân ly không hợp lý! Cần chọn lại.")
if check_run == 1:
    print("Okee! Thỏa mãn thuật toán Gradient-Descent")
