class Computer:
    #Everytime method/Function is called using object, init method is called
    def __init__(self):
        print ("Inside init method ")

    def config(self):
        print ("i5, 10th gen ,1TB")


if __name__ == '__main__':
    #Object Creation
    comp1 = Computer()
    comp2 = Computer()
    comp1.config()
    Computer.config(comp2)
