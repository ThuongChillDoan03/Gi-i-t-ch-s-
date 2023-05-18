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

###______________________________________MAIN_FUNCTION_________________________________###

n = len(matrix_test)
m = len(matrix_test[0])
def check_DK(m,n):
    if (n != (m - 1)):
        print("Không giòn! ko nên dùng Gauss-Jordan")
    if (n == (m-1)):
        print("Okee!Thực hiện PP GAUSS_JORDAN")


arr_remove_rows = []
arr_remove_cols = []
def choose_prioritize(n,matrix_test, arr_remove_rows, arr_remove_cols):
    for i in range(n):
        if i in arr_remove_rows:
            continue
        else:
            for j in range(n):
                if j in arr_remove_cols:
                    continue
                else:
                    absolute_value = 0
                    row = -1
                    col = -1
                    if np.abs(matrix_test[i][j]) == 1:
                        absolute_value = matrix_test[i][j]
                        row = i
                        col = j
                        return row,col
                    else:
                        if np.abs(matrix_test[i][j]) > np.abs(absolute_value):
                            absolute_value = matrix_test[i][j]
                            row = i
                            col = j
    return row, col

# row, col = choose_prioritize(n,matrix_test, arr_remove_rows, arr_remove_cols)

def change_matrix(matrix_test,n,row,col):
    for i in range(n):
        if i == row:
            continue
        const = (matrix_test[i][col])/(matrix_test[row][col])
        for j in range(n+1):
            matrix_test[i][j] -= const*matrix_test[row][j]
    return matrix_test

def check_num_elecols(matrix_test,n):
    check = 0
    for idx in range(n):
        array_row = np.where(matrix_test[idx][0:n] != 0)[0]
        if len(array_row) <= 1:
            continue
        else:
            check = 1
            break
    return check

check = check_num_elecols(matrix_test,n)
while(check == 1):
    row, col = choose_prioritize(n,matrix_test, arr_remove_rows, arr_remove_cols)
    matrix_test = change_matrix(matrix_test,n,row,col)
    arr_remove_rows.append(row)
    arr_remove_cols.append(col)
    # matrix_test = np.round(matrix_test,3)
    print("###_________________________________________________________________________###")
    print(matrix_test)
    check = check_num_elecols(matrix_test,n)

Solution = np.zeros(n)
for ind in range(n):
    arr_local = np.where(matrix_test[ind] != 0)[0]
    local = arr_local[0]
    Solution[local] = (matrix_test[ind][n])/(matrix_test[ind][local])
print("Nghiệm của hệ phương trình là:")
print(Solution)

