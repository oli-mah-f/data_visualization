import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    
    # previous points start to faint in color
    ax.scatter(rw.x_values, rw.y_values, 
               c=point_numbers, cmap=plt.cm.Blues, 
               edgecolors='none', s=15)
    
    #emphasize the first and last points
    ax.scatter(0,0, c='green', edgecolors='none', s=100) # starting point
    ax.scatter(rw.x_values[-1], rw.y_values[-1],
                c='red', edgecolors='none', 
                s=100) # ending point
    
    # hide axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input('Make another random walk? (y/n)')
    if keep_running == 'n': break