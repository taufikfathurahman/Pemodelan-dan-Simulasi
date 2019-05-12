import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import operator as op
from car_movement import *

def animate(i):
    cars_position = my_car_movement[i]
    car_marker.set_offsets(cars_position)
    return car_marker

if __name__ == "__main__":
    print('|===================================================|')
    print('|           Nagel Schreckenberg Simulation          |')
    print('|                       -----                       |')
    print('|===================================================|')
    print('> Input Parameter :                                ')
    M = int(input('$ M      :    '))
    p = float(input('$ p      :    '))
    v0 = int(input('$ v0     :    '))
    N = int(input('$ N      :    '))
    tmax = int(input('$ tmax   :    '))
    vmax = int(input('$ vmax   :    '))

    random.seed(4)
    car_road = np.array( [ [[0,M+0.5], [3,3]], [[0,M+0.5], [7,7]] ] )
    my_car = np.array([[random.randint(1,M), 5] for i in range(1,N+1)])
    my_car = np.array(sorted(my_car, key=op.itemgetter(0)))

    my_car_movement, i, count_dens, car_times = car_movement(M, p, v0, N, tmax, vmax, my_car)

    # Show kepadatan di posisi 80-90
    print()
    print('| ************************************************* |')
    print('|      Kepadatan Kedaraan di posisi X80 ~ X90:      |')
    print('| ************************************************* |')
    for x in count_dens:
        print(' $ Kepadatan kedaraan di waktu ke-'+str(x+1)+' adalah sebesar '+str(count_dens[x])+'%')

    print()
    print('| ************************************************* |')
    print('|            Waktu Rata Rata Kendaraan:             |')
    print('| ************************************************* |')
    for x in car_times:
        print('Waktu rata-rata mobil ke -', x+1, 'adalah', 100/(sum(car_times[x])/len(car_times[x])))

    fig = plt.figure()
    plot_axes = plt.axes(ylim=(0,10), xlim=(0,M+0.5))
    plt.plot([90,90],[3,7],color='yellow')
    plt.plot([80,80],[3,7],color='yellow')
    for road in car_road:
        plt.plot(road[0], road[1], color="black")
    car_marker = plot_axes.scatter([], [], s=75, marker="s")

    anim = animation.FuncAnimation(fig, animate, frames=len(my_car_movement), interval=50)
    plt.show()