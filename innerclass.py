class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.Laptop()

    def show(self):
        print (self.name, self.rollno)
        self.laptop.show()

    class Laptop:
        def __init__(self):
            self.name = "Hp"
            self.cpu = "i5"
            self.ram = 12

        def show(self):
            print (self.name, self.cpu, self.ram)


if __name__ == '__main__':
    s1 = Student("mahesh", 12)
    s2 = Student("sam", 32)
    s1.show()
    print (s1.laptop.name)
    print (s2.laptop.name)

    lap1 = Student.Laptop()
    print (lap1.name)
    lap1.show()
