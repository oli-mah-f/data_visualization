from random import choice

class RandomWalk:
    '''A class that generates random walks'''

    def __init__(self, num_points=5000):
        '''initialize walk attributes'''
        self.num_points = num_points

        # all walks start at (0,0)
        self.x_values = [0]
        self.y_values =[0]

    def fill_walk(self):
        '''calculates which points to go in random walks'''
        while len(self.x_values) < self.num_points:
            #which direction, and how far to go
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # reject if you don't take any steps
            if x_step == 0 & y_step == 0: continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


