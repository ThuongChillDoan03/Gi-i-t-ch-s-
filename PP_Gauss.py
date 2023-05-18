import pandas as pd
from pandas import ExcelFile
import numpy as np

data_frame = pd.read_excel("test_case_4.xlsx")
matrix_test = np.asarray(data_frame.astype(np.float64))

# print(data_frame)
print(matrix_test)
# print(matrix_case[1])
# print(matrix_case[0][0])

#NoTE: Nếu như muốn viết nghiệm ra cần bật lệnh np.round() để thực hiện làm tròn mới nhìn thấy nghiệm ko chứa e
#   matrix_test = np.round(matrix_test,3)

###___________________________________QUÁ_TRÌNH_THUẬN_________________________###

def check_column_element(idx,matrix_test):  #idx is column
    count = 0
    array_dif_0 = []
    for i in range(len(matrix_test)):
        if matrix_test[i][idx] != 0.0:
            array_dif_0.append(i)
            count += 1
    return array_dif_0,count

def check_rows(idx,matrix_test):
    cout = 0
    for check in range(len(matrix_test[idx])):
        if matrix_test[idx][check] != 0:
            cout += 1
    return cout

def row_nearest(idx,matrix_test):
    for jx in range(idx+1,len(matrix_test)):
        quantity = np.where(matrix_test[jx] != 0)[0]
        if len(quantity) > 0:
            return jx
    jx = 0
    return jx

def print_process_downstream_process(matrix_test):
    for idx in range(len(matrix_test)):
        array_dif_0,count = check_column_element(idx,matrix_test)
        array_dif_0 = np.array(array_dif_0)
        cout = check_rows(idx,matrix_test)
        jx = row_nearest(idx,matrix_test)
        if (cout == 0 and  jx != 0) or (matrix_test[idx][idx] == 0 and cout > 0 and jx != 0):  #đổi chỗ hàng dưới lên
            if (matrix_test[idx][idx] == 0) and (jx != 0) and (cout > 0):
                availabi = np.where(array_dif_0 > idx)[0]
                if len(availabi) > 0:
                    jx = array_dif_0[availabi[0]]
            arr_change = np.zeros(len(matrix_test[0]))
            for i in range(len(matrix_test[0])):
                arr_change[i] = matrix_test[idx][i]
            for j in range(len(matrix_test[0])):
                matrix_test[idx][j] = matrix_test[jx][j]
            for k in range(len(matrix_test[0])):
                matrix_test[jx][k] = arr_change[k]
            # matrix_test = np.round(matrix_test,3)
            print("Chuyển hàng thứ",jx+1,"thành hàng",idx+1,"_________________________________________________")
            print(matrix_test)


        if count > (idx+1):
            for id in range(idx+1,len(matrix_test)):
                coeffi = matrix_test[id][idx]/matrix_test[idx][idx]
                matrix_test[id] -= coeffi*matrix_test[idx]

        # print("Lần: ",idx+1,"_____________________________________________________________________")
        # for i in range(len(matrix_test)):
        #     matrix_test[i] = np.round(matrix_test[i],3)
        #     print(matrix_test[i])
        # matrix_test = np.round(matrix_test,3)
        print("Lần: ",idx+1,"_____________________________________________________________________")
        print(matrix_test)

def downstream_process(matrix_test):
    for idx in range(len(matrix_test)):
        array_dif_0,count = check_column_element(idx,matrix_test)
        array_dif_0 = np.array(array_dif_0)
        cout = check_rows(idx,matrix_test)
        jx = row_nearest(idx,matrix_test)
        if (cout == 0 and  jx != 0) or (matrix_test[idx][idx] == 0 and cout > 0 and jx != 0):  #đổi chỗ hàng dưới lên
            if (matrix_test[idx][idx] == 0) and (jx != 0) and (cout > 0):
                availabi = np.where(array_dif_0 > idx)[0]
                if len(availabi) > 0:
                    jx = array_dif_0[availabi[0]]
            arr_change = np.zeros(len(matrix_test[0]))
            for i in range(len(matrix_test[0])):
                arr_change[i] = matrix_test[idx][i]
            for j in range(len(matrix_test[0])):
                matrix_test[idx][j] = matrix_test[jx][j]
            for k in range(len(matrix_test[0])):
                matrix_test[jx][k] = arr_change[k]
            # matrix_test = np.round(matrix_test,3)

        if count > (idx+1):
            for id in range(idx+1,len(matrix_test)):
                coeffi = matrix_test[id][idx]/matrix_test[idx][idx]
                matrix_test[id] -= coeffi*matrix_test[idx]
            # matrix_test = np.round(matrix_test,3)
    matrix_BS = np.zeros((len(matrix_test),len(matrix_test[0])))
    for i in range(len(matrix_BS)):
        for j in range(len(matrix_BS[0])):
            matrix_BS[i][j] = matrix_test[i][j]
    return matrix_BS


###______________________________________QÚA_TRÌNH_NGHỊCH________________________________###

matrix_BS = downstream_process(matrix_test)
def rankA_BS(matrix_BS):
    rankbs = np.linalg.matrix_rank(matrix_BS)
    return rankbs

def rankA(matrix_BS):
    matrixA = np.zeros((len(matrix_BS),len(matrix_BS[0])-1))
    for i in range(len(matrixA)):
        for j in range(len(matrixA[0])):
            matrixA[i][j] = matrix_BS[i][j]
    ranka = np.linalg.matrix_rank(matrixA)
    return ranka

ranka = rankA(matrix_BS)
rankbs = rankA_BS(matrix_BS)
def main(matrix_BS,ranka,rankbs):
    if ranka != rankbs:
        print("Hệ phương trình vô nghiệm!!!")
    if (ranka == rankbs) and (ranka < (len(matrix_BS[0])-1)):
        print("Hệ phương trình có vô số nghiệm phụ thuộc vào: ", len(matrix_BS[0])-1-ranka, "tham số")
    if (ranka == rankbs) and (ranka == (len(matrix_BS[0])-1)):
        print("Hệ phương trình có nghiệm duy nhất:")
        vectors_X = np.zeros(len(matrix_BS[0])-1)
        a = len(matrix_BS)
        ele_value = matrix_BS[a-1][len(matrix_BS[a-1])-1]
        vectors_X[len(vectors_X)-1] = (ele_value)/(matrix_BS[a-1][a-1])
        for ind in range(1,a):    #a-1-ind
            ele_value = matrix_BS[a-1-ind][len(matrix_BS[a-1-ind])-1]
            sigsum_ = 0
            for ix in range(a-ind,len(matrix_BS[0])-1):
                sigsum_ += matrix_BS[a-1-ind][ix]*vectors_X[ix]
            vectors_X[a-1-ind] = (ele_value - sigsum_)/matrix_BS[a-1-ind][a-1-ind]
        return vectors_X
    return "OKiii!Đã xong:<3"

print_process_downstream_process(matrix_test)
print(main(matrix_BS,ranka,rankbs))
