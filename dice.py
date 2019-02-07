import random

class normal_die:
    def __init__(self):
        self.sides = ['straight road', 'curve road', '3 way road', 'straight rail', 'curve rail', '3 way rail']
    def roll(self):
        return random.choice(self.sides)

class special_die:
    def __init__(self):
        self.sides = ['overpass','curve connection','straight connection']
    def roll(self):
        return random.choice(self.sides)

if __name__ == '__main__':
    die = normal_die()
    print(die.roll())