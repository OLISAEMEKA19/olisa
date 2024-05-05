class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self):
        print("moving")

    def talk(self):
        print("talking")

    def vote(self):
        if self.age > 17:
            print("Eligible")
        else:
            print("Not Eligible")

daniel = Human(age=19, name="Daniel")
mary = Human(age=13, name="Mary")

print(daniel.name)
print(mary.name)

daniel.vote()
mary.vote()