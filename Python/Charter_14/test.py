def comparison(a, b):
    if a is b:
        print("a equally b")
    else:
        print("a not equally b")



class Square():
    square_list = []

    def __init__(self, w):
        self.weight = w
        self.square_list.append(self)
        print("""{} на {} на {} на {}""".format(self.weight, self.weight, self.weight, self.weight))