class car:
    def __init__(self):
        self.wheels= 4
        self.seats= 4

    def accelerate(self):
        print("accelerate")

    def brake(self):
        print("brake")

benz = car()
benz.accelerate()
benz.brake()
print(benz.seats)






