from copy import copy, deepcopy
import numpy as np
import numpy.random as random

def car_movement(M, p, v0, N, tmax, vmax, my_car):
    v = v0
    all_car_movement = []
    cars_order = [i for i in range(N)]
    time = 0
    count_dens = {}
    my_lst = {
        0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []
        }
    for x in range(tmax):
        x_row = []
        count_car = 0
        key = 0
        for i in cars_order:
            car = my_car[i]
            next_car = my_car[i+1 if i+1 < N else 0]
        
            v = np.min([v+1, vmax])
            if (next_car[0] < car[0]):
                d = M - next_car[0]
            else: 
                d = (next_car[0]-car[0])
            v = np.min([v, d-1])
            prob = random.rand()
            if (prob < p):
                v = np.max([0, v-1])

            x = copy(car[0])
            x = x + v
            if (x >= M):
                temp = []
                for i in range(N):
                    order = cars_order[i] + N-1
                    if (order + N-1 > N):
                        order = order - N
                    temp.append(order)
                cars_order = deepcopy(temp)
                x = x - M
            x_row.append(copy([x,car[1]]))

            if x >= 80 and x <= 90:
                count_car += 1

            my_lst[key].append(v)
            key += 1

        # Menghitung kepadatan
        count_dens[time] = ((count_car/10)*100)
        time += 1

        my_car = deepcopy(x_row)
        all_car_movement.append(deepcopy(x_row))

    return all_car_movement, i, count_dens, my_lst