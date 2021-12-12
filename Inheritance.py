class A:
    def __init__(self):
        pass

    def feature1(self):
        print ("Feature 1 is working.")

    def feature2(self):
        print ("Feature 2 is working.")


# Single Level Inheritance
class B(A):
    def __init__(self):
        pass

    def feature3(self):
        print ("Feature 3 is working.")

    def feature4(self):
        print ("Feature 4  is working.")


# Multilevel Inheritance
class C(B):
    def __init__(self):
        pass

    def feature5(self):
        print ("Feature 5 is working.")


# Multiple Inheritance
# class A:
# class B:
# class C(A,B)

if __name__ == '__main__':
    a1 = A()
    a1.feature1()
    a1.feature2()

    b1 = B()
    b1.feature3()
    b1.feature4()

    b1.feature1()
    b1.feature2()

    c1 = C()
    c1.feature1()
    c1.feature3()
    c1.feature5()
