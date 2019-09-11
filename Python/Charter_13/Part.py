class Share():
    def __init__(self):
        pass

    def what_am_i(self):
        print("i am Share")


class Rectangle(Share):
    def __init__(self, w , h):
        self.weight = w
        self.height = h

    def calculate_perimeter(self):
        return self.weight * 2 + self.height * 2


rect = Rectangle(7, 5)



class Square(Share):
    def __init__(self, w):
        self.weight = w

    def calculate_perimeter(self):
        return self.weight * 4

    def change_size(self, new_size):
        self.weight += new_size

sq= Square(3)


class Horse():
    def __init__(self, name):
        self.name = name

class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse
pony = Horse("Sunny")
owned_rider = Rider("Bunny", pony)

print(owned_rider.horse.name)
