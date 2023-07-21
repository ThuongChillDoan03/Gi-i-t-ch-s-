# Khai báo thư viện
import numpy as np
import  math
import sys

# Load file
f = open("Test_data_xuongthang.txt", "r")
temp = sys.stdout                 # store original stdout object for later
sys.stdout = open('output.txt', 'w')
a = f.readline()
n =  int(a)
print('Ma tran co: {} x {}'.format(n, n))
b = f.readline()
b = b.split()
X = []
for i in (b):
    X.append(float(i))
X = np.array(X)
Y = X.reshape(n, 1)
c = f.read()
c = c.split()
A = []
G = []
for i in c:
    A.append(float(i))
    G.append(float(i))
G = np.array(G).reshape(n, n)
A = np.array(A).reshape(n, n)
#G = np.array(G).reshape(n, n)
print('Ma tran A la: ')
print(A)
print('_'*100)
E = 0.001


#Chuẩn hóa
def Chuan_Hoa(M):
    maxi = abs(M[0][0])
    c = M[0][0]
    for i in range (len(M)):
        if maxi < abs(M[i][0]):
            maxi = abs(M[i][0])
            c = M[i][0]
    matrix = M / c
    return matrix



#Kiểm tra
def Kiem_tra(B, m, n):
    A = B[m] - B[n]
    return max(abs(A))

#Lũy thừa
def Luy_thua(A, B, m):
    M = A.dot(B[m])
    return M
    #B= B[m-1] . A


#Xử lí
def Xu_li(A, Y):
    B = []
    B.append(Y)
    Z = np.zeros((n, 1))
    B.append(Chuan_Hoa(Luy_thua(A, B, 0)))
    B.append(Chuan_Hoa(Luy_thua(A, B, 1)))
    B.append(Chuan_Hoa(Luy_thua(A, B, 2)))
    m = 3
    TH = 4
    while True:
        M = []
        F = B[-1]
        # for i in range (len(F)):
        #     x = round(F[i][0], 4)
        #     M.append(x)
        #M = np.array(M).reshape(n, 1)
        if sum(F == Z) == n:
            sys.exit()
        if m == 218:    # THAY DOI SO LAN LAP O DAY !!!!!!!!!!!!!!!!!!!!!!!!
            break
        if Kiem_tra(B, m - 1, m - 2) <= E:
            TH = 1
            break
        if Kiem_tra(B, m  - 1, m - 3) <= E:
            TH = 3
            break
        B.append(Chuan_Hoa(Luy_thua(A, B, m)))
        m += 1
    return m, TH, B


#Chuyển ma trận xuống thang
def Chuyen_MT(A, VTR):
    B = A
    V = VTR.reshape(n,)
    theta = np.eye(n, dtype=float)
    Vmax = max(V)
    loca = 0
    for i in range (n):
        if V[i] == Vmax:
            loca += i
            break
    E = theta[: , loca : loca +1] - VTR.reshape(n, 1)
    theta[:, loca : loca +1] = E
    print("\n")
    print("\n********************* THUC HIEN XUONG THANG *************************")
    print("Ma tran theta dung de thuc hien xuong thang la: ") ############################
    print(theta)
    A = theta.dot(A)
    # print(loca)
    # sys.exit()
    return loca , A

def timVchuan(lam, lamt, vec, vect, w):
    if lam == lamt:
        return vec
    elif lam != lamt:
        E = np.eye(n)
        v_w = G  - lam * E
        v_w =  v_w.dot(vec)
        c = v_w[w][0] / (lam - lamt)
        return vec + c * vect

# c = ((A - lamda * E)* theta * V')w / (lam - lamt)


#Tìm
C=[]
D=[]
for i in range(n):
    m, TH, B = Xu_li(A, Y)
    if i >= 1 :
        print("Ma tran A sau khi xuong thang: ")
        print(A)
        print("\n")

    if TH == 1:
        VTR = B[-1]
        #VTRt = B[-2]
        VTR_T = VTR.reshape(1, n)
        AX = A.dot(VTR)
        XTAX = (VTR_T.dot(AX))
        XTX = (VTR_T.dot(VTR))
        lamda = XTAX[0] / XTX[0]
        lamda = round(lamda[0], 4)
        # C.append(lamda)
       # > VTR chuwa C, >lamda2 chuan
        print("TH1")
        for j in range(len(B)):
            print("A{}Y = ".format(j))
            print(B[j])
            print("\n")
        print('Sau {} lan lap'.format(m))
        print('Gia tri rieng thu {} la: '.format(i+1), lamda)
        print('Vector rieng tuong ung la: ')
        #print(VTR)
        VTRc= VTR
        if i >= 1:
            VTRc = timVchuan(lamda, C[-1], VTR, D[-1], loca)
        D.append(VTRc)
        C.append(lamda)
        print(Chuan_Hoa(VTRc))
        loca, A = Chuyen_MT(A, VTR)
        Y = np.random.rand(n, 1)
        print('_' * 100)


    elif TH == 3:
        print("TH3")
        for j in range(len(B)):
            print("A{}Y = ".format(j))
            print(B[j])
            print("\n")
        AmY = A.dot(B[-1])
        Am1Y = A.dot(AmY)
        Am2Y = A.dot(Am1Y)
        lamda_N = 0
        lamda_N1 = -1e18-1
        lamda_N2 = 1e18+1
        for j in range (n):
            if AmY[j][0] == 0:
                continue
            lamda_N1 = max((Am2Y[j][0]) / (AmY[j][0]), lamda_N1)
            lamda_N2 = min((Am2Y[j][0]) / (AmY[j][0]), lamda_N2)
            if abs(lamda_N2) > abs(lamda_N1):
                lamda_N = lamda_N2
            else:
                lamda_N = lamda_N1
        lamda_N = math.sqrt(lamda_N)
        if i >=1:
            if round(lamda_N, 1) == round(C[-1], 1):
                lamda_N = - lamda_N
        VTR_N = Am1Y + lamda_N * AmY
        VTR_N = Chuan_Hoa(VTR_N)
        #TR_N = Chuan_Hoa(VTR_N)
        print("THUOC TH3")
        print('Sau {} lan lap'.format(m))
        print('Gia tri rieng la: ', round(lamda_N, 4))
        print('Vector tuong ung la: ')
        VTRc= VTR_N
        if i >= 1:
            VTRc = timVchuan(lamda_N, C[-1], VTR_N, D[-1], loca)
        D.append(VTRc)
        C.append(lamda_N)
        print(Chuan_Hoa(VTRc))
        loca, A = Chuyen_MT(A, VTR_N)
        Y = np.random.rand(n, 1)
        print('_' * 100)

    elif TH == 4:
        print("TH4")
        for j in range(len(B)):
            if j == 0:
                print("Y =")
            else:
                print("A{}Y = ".format(j))
            print(B[j])
            print("\n")
        AmY = B[-1]
        Am1Y = A.dot(AmY)
        Am2Y = A.dot(Am1Y)
        a_1 = Am2Y[0][0]
        a_2 = Am2Y[1][0]
        b_1 = Am1Y[0][0]
        b_2 = Am1Y[1][0]
        c_1 = AmY[0][0]
        c_2 = AmY[1][0]
        a = (c_1 * b_2 - b_1 * c_2)
        b = (a_1 * c_2 - c_1 * a_2)
        c = (b_1 * a_2 - a_1 * b_2)
       # b= str(b)
        #c= str(c)
        print("TH4")
        print('Ta thu duoc phuong trinh: Z^2 + {0}Z + {1} = 0 '.format(str(b), str(c)))
        denta = b ** 2 - 4 * a * c
        if denta >= 0:
            print('Phuong trinh co denta >= 0')
        else:
            lamda_1 = complex(-b / (2 * a), -math.sqrt(abs(denta)) / (2 * a))
            lamda_2 = complex(-b / (2 * a), math.sqrt(abs(denta)) / (2 * a))
            VTR_1 = Am1Y - lamda_1 * AmY
            VTR_2 = Am1Y - lamda_2 * AmY
            print('Gia tri rieng la: {}'.format(lamda_1))
            print('Vector rieng tuong ung la: ')
            print(VTR_1)
            print('*' * 100)
            print('Gia tri rieng la: {}'.format(lamda_2))
            print('Vector rieng tuong ung la: ')
            print(VTR_2)
        # A = Chuyen_MT(A, VTR_1)
        # Y = np.random.rand(n, 1)
        break

sys.stdout.close()
sys.stdout = temp