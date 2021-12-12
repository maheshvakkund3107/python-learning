class Car:
    # Variables defined outside a init method and inside class are class variables
    # Stored inside Class Name Space
    wheels = 6

    # Variables defined inside a init method are instance variables
    # Stored inside Inside Name Space
    def __init__(self):
        self.mileage = 10
        self.company = "BMW"


if __name__ == '__main__':
    c1 = Car()
    c2 = Car()
    c1.mileage = 20
    print (c1.mileage, c1.company, c1.wheels, Car.wheels)
    print (c2.mileage, c2.company, c2.wheels, Car.wheels)
