class Student:
    school = 'Kle'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Getters are accessors.
    def get_m1(self):
        return self.m1

    # Setters are mutators.
    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print ("This is a Student Class")


if __name__ == '__main__':
    s1 = Student(34, 45, 65)
    s2 = Student(12, 23, 56)
    s3 = Student(45, 64, 52)
    print (s1.avg())
    print (s2.avg())
    print (s3.avg())
    print (s1.get_m1())
    s1.set_m1(4)
    print (s1.m1)
    print (Student.getSchool())
    Student.info()
