import sympy as sym
import scipy as sci
import numpy as np
from math import *
import sys


# ===================================================================================
# Phần thuật toán chính
class newton_mat_inversion:
    # {
    max_attempt = 2;

    def __init__(self, A, n, eps):  # Khởi tạo
        # {
        self.A = np.reshape(np.array(A), (n, n));
        self.n = n;
        self.eps = eps;
        self.nr_iterations = 0;

    # }
    def norm(self, __A, __norm_type=2):  # Chuẩn ma trận
        # {
        return np.linalg.norm(__A, __norm_type);

    # }
    def __refine_initial_approx(self):  # Tìm xấp xỉ đầu:
        # {
        # Gán các biến cơ bản
        E = np.eye(self.n);
        A = self.A;
        X = self.A;

        # PP xấp xỉ đầu của Pan & Reif
        t1 = self.norm(X, 1);
        t2 = self.norm(X, inf);
        X = (X / (t1 * t2)).T;

        # Hiệu chỉnh lại giá trị q của ma trận xấp xỉ đầu
        attempt = 0;
        while (attempt <= newton_mat_inversion.max_attempt):
            # {
            X = X @ (2 * E - A @ X);
            if (self.norm(E - A @ X) < 1): attempt += 1;
            self.nr_iterations += 1 * bool(attempt == 0);
        # }

        # Trả về ma trận xấp xỉ đầu
        return X;

    # }
    def __pure_newton(self, X_0):  # Lặp Newton nguyên bản
        # {

        # Gán các biến cơ bản
        norm_X0 = self.norm(X_0);  # Do X_0 không đổi nên ta đặt 1 biến làm chuẩn của X_0
        E = np.eye(self.n);
        A = self.A;
        eps = self.eps;

        # Bước 2 của thuật toán
        q2k = q = self.norm(E - A @ X_0);
        X = X_0;

        # Kiểm tra điều kiện hội tụ
        if (q >= 1):
            # {
            print("Xấp xỉ đầu không thỏa mãn nên không đưa ra được ma trận nghịch đảo.");
            return np.full((self.n, self.n), float("NaN"));
        # }

        # Lặp
        while (norm_X0 * q2k >= self.eps * (1 - q)):
            # {
            self.nr_iterations += 1;
            X = X @ (2 * E - A @ X);
            print("lan lap thu ", self.nr_iterations, ": ")
            print(X)
            print(" ")
            q2k = q2k ** 2
        # }

        # Đưa ra ma trận cuối cùng
        print(f"Phương pháp Newton kết thúc sau {self.nr_iterations} bước lặp", file=sys.stderr);
        return X;

    # }

    def improved_newton(self):  # PP Newton cải tiến với xấp xỉ đầu
        # {
        if (np.linalg.det(self.A) == 0):
            # {
            print("A không khả nghịch nên không đưa ra được ma trận nghịch đảo");
            return np.full((self.n, self.n), float("NaN"));
        # }
        return self.__pure_newton(self.__refine_initial_approx());

    # }
    def pure_newton(self, X_0):  # PP Newton nguyên bản
        # {
        if (np.linalg.det(self.A) == 0):
            # {
            print("A không khả nghịch nên không đưa ra được ma trận nghịch đảo");
            return np.full((self.n, self.n), float("NaN"));
        # }
        return self.__pure_newton(X_0);
    # }
# }