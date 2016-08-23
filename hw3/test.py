count = 0

class a:
    def __init__(self):
        global count
        print (count)

b = a()
c = []
c.append(b)
c.append(b)
d = c
