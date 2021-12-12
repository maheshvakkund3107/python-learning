class Computer:
    def __init__(self):
        self.name = "Mahesh"
        self.age = 25

    def update(self):
        self.name = "Abcd"

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


if __name__ == '__main__':
    comp1 = Computer()
    comp2 = Computer()
    comp1.name = "Sam"
    comp1.age = 25
    print(comp1.name)
    print(comp2.name)
    comp1.update()
    print (comp1.name)
    if comp1.compare(comp2):
        print ("They are same Ages")
    else:
        print ("They are different Ages")
