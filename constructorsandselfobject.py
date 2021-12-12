class Computer:
    def __init__(self):
        self.name = "Mahesh"
        self.age = 25

    def update(self):
        self.name = "Abcd"


if __name__ == '__main__':
    comp1 = Computer()
    comp2 = Computer()
    comp1.name = "Sam"
    comp1.age = 27
    print(comp1.name)
    print(comp2.name)
    comp1.update()
    print (comp1.name)
