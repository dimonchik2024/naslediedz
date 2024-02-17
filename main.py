class Apple:
    def __init__(self):
        self.cameras = 3
        self.logotype = "apple"
        self.company = "apple"
class proshooting:
    def __init__(self):
        super().__init__()
        self.proshooting = "proshooting"
        self.fourk = "Have 4k Camera"
class phone(Apple, proshooting):
    def printer(self):
        print(self.cameras)
        print(self.logotype)
        print(self.company)
        print(self.proshooting)
        print(self.fourk)
Apple = phone()
Apple.printer()