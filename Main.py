# class defining
class Matrix:
    # __init__ ---> Constructor-->that execute the method as soon as the object of the class is created
    # special/magic/dunder method
    #self is object and we can say object is self

    def __init__(self,mat):
        self.mat=mat
        self.rows = len(mat)
        self.cols = len(mat[0])

    #__str__ --> special method which defines how the data type looks like
    def __str__(self):
        res=""
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                res+=str(self.mat[i][j])+" "
            res+="\n"
        return res

    def __add__(self,other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same number of rows and columns")
        else:
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                        self.mat[i][j]+=other.mat[i][j]

Mat1=Matrix([[1,3,3,5],[1,2,3,4]])
Mat2=Matrix([[1,3,5,7],[2,3,4,5]])
print(Mat1+Mat2)