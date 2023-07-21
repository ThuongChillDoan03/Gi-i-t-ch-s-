from cmath import sqrt
import pandas as pd
from pandas import ExcelFile
import numpy as np

"''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"

def cholesky1():
    A1=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            A1[i][j]=sum(A[k][i]*A[k][j] for k in range(n))
    return A1
"''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"
def cholesky2():
    B1=[0]*n
    for i in range(n):
        B1[i]=sum(A[k][i]*B[k] for k in range(n))
    return B1
"''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"
def cholesky():
    S=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            tổng = sum(S[k][i] * S[k][j] for k in range(j))
            if abs(tổng- A1[i][i])<0.0000000001:
                break
            if i==j:
                S[j][i] = sqrt(A1[i][i] - tổng)
            else:
                S[j][i] = (A1[j][i] - tổng)/S[j][j]
        if S[i][i]==0:
            break
    return S
"''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"
def cholesky3():
    Y=[0]*n
    for i in range(n):
        Y[i]=(B1[i]-sum(S[k][i]*Y[k] for k in range(i)))/S[i][i]
    return Y
"''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"
def cholesky4():
    X=[0]*n
    for i in range(1, n+1):
        X[-i]=(Y[-i]-sum(S[-i][-k]*X[-k] for k in range(1, i)))/S[-i][-i]
    return X
"''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"
file = pd.read_excel("Data_Cholesky.xlsx")
matrix = np.asarray(file.astype(np.float64))
n=len(matrix)
A=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        A[i][j]=float(matrix[i][j])
print('A= ')
for i in A:
    print(i)
"''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"
B=[0]*n
for i in range(n):
    B[i]=float(matrix[i][n])
print('B= ')
for i in B:
    print(i)
"''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"
print('')
print('Giải hệ phương trình tuyến tính bằng phương pháp Cholesky: AX=B')
"''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"
print('')
print('Tìm ma trận A1 đối xứng:')
m=1
for i in range(n):
    for j in range(n):
        if A[i][j]==A[j][i]:
            m*=1
        else:
            m*=0
if m==1:
    print('A là ma trận vuông đối xứng có thể khai triển theo Cholesky')
    A1=A
    B1=B
else:
    print('A không đối xứng')
    print('Để giải được theo Cholesky ta cần nhân cả 2 vế với A^t:')
    A1=cholesky1()
    B1=cholesky2()
print('')
print('Khi đó phương trình trở thành A1*X=B1, với: ')
print('A1= ')
for i in A1:
    print(i)
print('và B1= ')
for i in B1:
    print(i)
S=cholesky()
if S[n-1][n-1]==0:
    print('Ma trận A1 có định thức bằng 0 nên không thể khai triển Cholesky')
    print('Suy ra phương trình AX=B không có nghiệm duy nhất')
else:
    print('')
    print('Phân tích A1 theo Cholesky: A1=S^t*S')
    print('S= ')
    for i in S:
        print(i)
    print('')
    print('Khi đó phương trình trở thành: S^t*S*X=B1')
    print('Đặt Y=S*X có:  S^t*Y=B1')
    print('Giải phương trình này ta được: ')
    Y=cholesky3()
    print('Y= ')
    for i in Y:
        print(i)
    print('')
    print('Giải phương trình SX=Y ta được nghiệm của phương trình:')
    X=cholesky4()
    print('X= ')
    for i in X:
        print(i)