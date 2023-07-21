from cmath import sqrt
import pandas as pd
from pandas import ExcelFile
import numpy as np


np.set_printoptions(suppress=True, linewidth=np.inf, precision=6)
def cholesky():
    S=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            tổng = sum(S[k][i] * S[k][j] 
                       for k in range(j))
            if abs(tổng - A1[i][i]) == 0: 
                break
            if i == j: 
                S[j][i] = sqrt(A1[i][i] - tổng)
            else: 
                S[j][i] = (A1[j][i] - tổng)/S[j][j]
        if S[i][i] == 0: 
            break
    return S
def cholesky3(): #Hàm giải phương trình BY = E
    Y = np.zeros([n, n],dtype="complex_")
    for i in range(n-1, -1, -1):
        for j in range(i,n):
            if j == i: 
                Y[i,j] = 1/S[i,j]
            if j>i:
                Y[i, j] = (B1[i,j]-sum(S[i][k]*Y[k,j] 
                                       for k in range(i+1,n)))/S[i][i]
    return Y

#Nhập ma trận
# A = np.loadtxt("input2.txt",dtype='complex', delimiter=' ') #Input
file = pd.read_excel("Data_NĐảo.xlsx")
A = np.asarray(file.astype(np.float64))

k=0
print('Ma trận đầu vào là :')
print(A)
n = len(A)
B = np.zeros([n,n])
for i in range(n):
    B[i,i] = 1.0
m = 1
for i in range(n):
    for j in range(n):
        if A[i][j] == A[j][i]: continue
        else: m *= 0
if m == 1:
        A1=A
        B1=B
else:
        A1 = A.dot(np.transpose(A))
        B1 = B
        k = 1
S = np.array(cholesky())
print("==============================================================")
print("ma tran S la:")
print(S)
if S[n-1][n-1] == 0:
    print('Ma trận A1 có định thức bằng 0 nên không thể khai triển Cholesky')
    quit()
Y = cholesky3()
print("=============================================================")
print('Ma trận nghịch đảo là:')
if k == 0:
    print(Y)
if k == 1:
    Y = np.transpose(A).dot(Y)
    print(Y)
print('===============================================================')