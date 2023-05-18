import pandas as pd
from pandas import ExcelFile
import numpy as np

data_frame = pd.read_excel("Check_Gauss.xlsx")
matrix_case = np.asarray(data_frame)

print(data_frame)
print(matrix_case)
print(type(matrix_case[0][0]))
# print(matrix_case[1])
# print(matrix_case[0][0])
