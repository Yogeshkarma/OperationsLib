# class defining
class Matrix:
    # __init__ ---> Constructor-->that execute the method as soon as the object of the class is created
    # special/magic/dunder method
    # self is object and we can say object is self
    # instance variable--> the variable for which the value of that is different for different objects

    def __init__(self, mat):
        self.mat = mat
        self.__rows = len(mat)
        self.__cols = max(len(row) for row in mat)  #fixed with len(mat[0])

    #__str__ --> special method which defines how the data type looks like
    def __str__(self):
        res = ""
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                res += str(self.mat[i][j]) + " "
            res += "\n"
        return res

    def __add__(self, other):
        if self.__rows != other.__rows or self.__cols != other.__cols:
            raise ValueError("Matrices must have same number of rows and columns")
        else:
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    self.mat[i][j] += other.mat[i][j]
            return Matrix(self.mat)

    def __sub__(self, other):
        if self.__rows != other.__rows or self.__cols != other.__cols:
            raise ValueError("Matrices must have same number of rows and columns")
        else:
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    self.mat[i][j] -= other.mat[i][j]
            return Matrix(self.mat)

    def __mul__(self, other):
        if self.__cols != other.__rows:
            raise ValueError("Matrix multiplication is not possible")
        else:
            #bug here
            result_data = []
            for i in range(self.__rows):
                result_row = []
                for j in range(other.__cols):
                    sum_product = 0
                    for k in range(self.__cols):
                        sum_product += self.mat[i][k] * other.mat[k][j]
                    result_row.append(sum_product)
                result_data.append(result_row)
            return Matrix(result_data)

    def transpose(self):
        transposed_mat = []
        for i in range(self.__cols):
            transposed_row = []
            for j in range(self.__rows):
                transposed_row.append(self.mat[j][i])
            transposed_mat.append(transposed_row)
        return Matrix(transposed_mat)


Mat1 = Matrix([[1, 3, 2], [3, 4, 5]])
Mat2 = Matrix([[1, 1, 1], [1, 1, 1]])
print(Mat1)
print(Mat1.transpose())
