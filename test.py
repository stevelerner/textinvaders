class alien:
    def __init__(self, y, x, life):
        self.y = y
        self.x = x
        self.life = life
        alien.endtime = time.time() + self.life

    def displayEndtime(self):
        print("Endtime: ", alien.endtime)
