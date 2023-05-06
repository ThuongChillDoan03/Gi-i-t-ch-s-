# Hậu nghiệm
import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.lib import scimath
import timeit

# Nhập vào hàm số
def f(x):
    return np.log(x) - 1

# Bisection method
def bisection():
    def try_():
        print("----------------------------------------------------------------------")
        print("Bạn có muốn sử dụng lại chương trình bisection method không? Yes/No? Y/N?")
        request = str(input())
        a = request.upper()
        if (a == 'YES' or a == 'Y'):
            bisection()
        elif (a == 'NO' or a == 'N'):
            print("Cảm ơn. Hẹn gặp lại ♥ ")

    try:
        print("Khoảng cách ly nghiệm là khoảng sao trong khoảng a, b có duy nhất 1 nghiệm của phương trình")
        print("Xác định cận dưới a của khoảng cách ly nghiệm. ")
        a = float(input("a = "))
        print("Xác định cận trên b của khoảng cách ly nghiệm. ")
        b = float(input("b = "))
        print("Độ chính xác epsilon.")
        eps = float(input("epsilon = "))
    except:
        print("----------------------------------------------------------------------")
        print("Yêu cầu xác định lại khoảng cách ly nghiệm hoặc epsilon (số thực).")
        print("Vui lòng xác định lại.")
        bisection()
    else:
        if (a >= b or eps >= 1 or eps <= 0):
            print("----------------------------------------------------------------------")
            print("Yêu xác định lại a < b và epsilon < 1 và khác epsilon >.")
            bisection()
        elif (f(a) * f(b) >= 0):
            print("----------------------------------------------------------------------")
            print("Khoảng cách ly nghiệm không hợp lệ yêu cầu xác định lại.")
            bisection()
            # Vì đã kiểm tra điều kiện nghiêm ngặt của a, b ở trên nên chắc chắn rằng a thỏa mãn khoảng cách ly
        elif (f(a) * f((a + b) / 2) == 0):
            print("Nghiệm gần đúng của phưởng trình là: ", ((a + b) / 2))
            print("Số lần lặp là: 1 lần")
            try_()

        # Bisection-Method
        else:
            # làm tròn eps
            e = eps
            demss = 0
            while e < 1:
                demss += 1
                e *= 10
            # Lặp đến khi sai số tuyệt đối < sai số cần tìm thì dừng.

            #Tạo bảng xét các lần lặp
            count = 0
            print("{0:^15}|{1:^15}|{2:^15}|{3:^15}|{4:^15}|{5:^15}|{6:^15}".format("Số lần lặp", "a", "b", "c", "f(a)",
                                                                                   "f(b)", "f(c)"))
            #Phương pháp
            while ((math.fabs(b - a)/2.0)> eps):
                c = (a + b) / 2.0
                mid = f(a) * f(c)
                print("{0:^15}|{1:<15}|{2:<15}|{3:<15}|{4:<15}|{5:<15}|{6:<15}".format(count, round(a, demss),
                                                                                       round(b, demss),
                                                                                       round(((a + b) / 2), demss),
                                                                                       round(f(a), demss),
                                                                                       round(f(b), demss),
                                                                                       round(f((a + b) / 2), demss)))
                if (mid > 0):
                    a = c
                elif (mid < 0):
                    b = c
                else:
                    print("- Số lần lặp: ", count)
                    print("=> Nghiệm gần đúng của phương trình là: x =  ", round(c, demss))
                    try_()
                count += 1
            print("- Số lần lặp: ", count)
            print("=> Nghiệm gần đúng của phương trình là: x =  ", round(c, demss))
            start = timeit.default_timer()
            stop = timeit.default_timer()
            print('- Time: ', (stop - start) * 1000, "ms")
            try_()
bisection()