def styleListMaker():
    for i in range(self.level + 9):
        x = random.randint(40, self.width - 140)
        y = random.randint(40, self.height - 140)
        self.styleList.append(Style(x, y, 800, 600, self.currDifficulty))
