import random

# class
class RandomWalk():

    def __init__(self, steps=1000):
        self.steps = steps
        self.x = [0]
        self.y = [0]

    def walk(self):
        counts = 0
        while counts < self.steps:
            dx = random.uniform(-1, 1)
            dy = random.uniform(-1, 1)
            if dx == 0 and dy == 0:
                continue
            self.x.append(self.x[-1] + dx)
            self.y.append(self.y[-1] + dy)
            counts += 1

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


# plot
import matplotlib.pyplot as plt

stumbler = RandomWalk()
stumbler.walk()
x = stumbler.get_x()
y = stumbler.get_y()

plt.plot(x, y, color='grey')
plt.plot(x[0], y[0], marker='o', markerfacecolor='blue')
plt.plot(x[-1], y[-1], marker='o', markerfacecolor='red')
plt.show()