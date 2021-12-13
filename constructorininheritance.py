class A:
    def __init__(self):
        print ("IN A INIT")

    def feature1(self):
        print ("Feature 1 is working.")

    def feature2(self):
        print ("Feature 2 is working.")


# Single Level Inheritance
class B(A):

    # If Init of B is not available then it will call init of A.
    # If Init of Subclass is not available it will call init of Superclass.
    # But if we still need to call the init of superclass we need to use the keyword super
    def __init__(self):
        A.__init__(self)
        print ("IN B INIT")

    def feature3(self):
        print ("Feature 3 is working.")

    def feature4(self):
        print ("Feature 4  is working.")


if __name__ == '__main__':
    a1 = B()
