class Pycharm:
    def __init__(self):
        pass

    @staticmethod
    def execute():
        print ("compile")
        print ("running")


class MyEditor:
    def __init__(self):
        pass

    @staticmethod
    def execute():
        print ("spell check")
        print ("convention check")
        print ("compile")
        print ("running")


class Laptop:
    def __init__(self):
        pass

    @staticmethod
    def code(ides):
        ides.execute()


if __name__ == '__main__':
    ide = MyEditor()
    ide1 = Pycharm()

    lap = Laptop()
    lap.code(ide)
    lap.code(ide1)
