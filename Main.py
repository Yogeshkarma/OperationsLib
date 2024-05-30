# class defining
class MatOps:
    # __init__ ---> Constructor-->that execute the method as soon as the object of the class is created
    def __init__(self):
        self.mat1 = list()
        self.mat2 = list()
        self.Options()

    def Options(self):
        user_input = input("""What Operations you want to do!
        1.Single Matrix Operation
        2.Dual Matrix Operation
        3.Exit""")
        if (user_input == '1'):
            self.Single_Matrix_Ops()
        elif (user_input == '2'):
            pass
        elif (user_input == '3'):
            pass
        else:
            print('try again')
    def Single_Matrix_Ops(self):
        u_input=input("""what Operation would you like to do?
        1.Transpose of a matrix
        2.Adjoint of a matrix
        """)
        if(u_input == '1'):
            print('you have chosen adjoint')
        elif(u_input == '2'):
            print('you have chosen transpose')


Mat=MatOps()
print(Mat)