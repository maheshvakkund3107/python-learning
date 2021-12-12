class Computer:
    def __init__(self):
        pass

    def config(self):
        print ("i5, 10th gen ,1TB")


if __name__ == '__main__':
    comp1 = Computer()
    comp2 = Computer()
    comp1.config()
    Computer.config(comp2)
