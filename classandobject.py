class Computer:
    # Everytime method/Function is called using object, init method is called
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print ("Config is:", self.cpu, self.ram )


if __name__ == '__main__':
    # Object Creation
    comp1 = Computer("i5", 16)
    comp2 = Computer("Ryzen", 32)
    comp1.config()
    Computer.config(comp2)
