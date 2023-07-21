import sympy as sym
import scipy as sci
import numpy as np
import pandas as pd
from pandas import ExcelFile
from math import *
import sys

from Lib_newton_GĐ import *

A             = np.zeros((1,0))
n             = 0
eps           = 0
wholeSize     = 1


# Load ma trận từ file
while(n * n != wholeSize):
#{
    print("Đang tải ma trận.....")
    file = pd.read_excel("Data_NĐảo.xlsx")
    A = np.asarray(file.astype(np.float64))
    A = np.ravel(A)

    # Tự sinh kích thước ma trận
    wholeSize = np.shape(A)[0]
    n = int(sqrt(wholeSize))


    if (n * n != wholeSize):
    #{
        c = input("Kích cỡ ma trận không hợp lệ. Vui lòng chỉnh sửa file input.txt gõ \"Y\" để tải lại chương trình hoặc gõ \"N\" để thoát chương trình:")
        if(c == "N"):
            exit()
    #}
    else:
        A = np.reshape(A, (n,n))
        print("Tải ma trận thành công.")
#}


# Nhập sai số eps
eps           = float(input("Nhập sai số eps: "))

# In ra ma trận A
print("--------------------------------------------------------------------")
print("Ma trận A:")
print(A)
print("--------------------------------------------------------------------")

# Nghịch đảo ma trận
uu = newton_mat_inversion(A, n, eps)

# In ra ma trận nghịch đảo
print("--------------------------------------------------------------------")
A1 = uu.improved_newton()
print("Ma trận nghịch đảo của A:")
print(A1)

# Kiểm tra nhân ngược
print("--------------------------------------------------------------------")
print("Kiểm tra nhân ngược:")
print(A1 @ A)