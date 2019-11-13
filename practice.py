class a():
    def __init__(self, x, y):
        self.location = [x, y]

b = a('a', 1)
c = a('b', 2)
d = a('c', 3)
list = [b, c, d]

for i in list:
    if i.location == ['a', 1]:
        print(i.location)