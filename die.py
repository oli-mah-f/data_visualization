from random import randint
print(randint(1, 5))

class Die:
    '''to represent a single die'''
    
    def __init__(self, num_sides=6):
        '''initialize die attributes'''
        self.num_sides = num_sides

    def roll(self):
        '''return a random int, representing die's side number'''
        return randint(1, self.num_sides)
    
