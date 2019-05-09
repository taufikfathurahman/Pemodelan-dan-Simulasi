import time 

def make_car_model(my_car):
    car1 = my_car(-40, 155, -20, 170, fill='blue')
    car2 = my_car(-20, 155, 0, 170, fill = 'green')
    car3 = my_car(1000, 180, 1020, 195, fill = 'red')
    car4 = my_car(1040, 180, 1060, 195, fill = 'cyan')
    car5 = my_car(-120, 155, -100, 170, fill = 'orange')
    car6 = my_car(-160, 155, -140, 170, fill = 'maroon')
    car7 = my_car(1120, 180, 1140, 195, fill = 'yellow')
    car8 = my_car(1200, 180, 1220, 195, fill = 'pink')
    car9 = my_car(-300, 155, -280, 170, fill = 'gold')
    car10 = my_car(1320, 180, 1340, 195, fill = 'purple')

    return [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]

def set_car_speed(car):
    car[0].car_speed(3,0)
    car[1].car_speed(5,0)
    car[2].car_speed(-5,0)
    car[3].car_speed(-3,0)
    car[4].car_speed(4,0)
    car[5].car_speed(3,0)
    car[6].car_speed(-4,0)
    car[7].car_speed(-3,0)
    car[8].car_speed(5,0)
    car[9].car_speed(-4,0)

    return car

def car_movement(car, x):
    time.sleep(0.005)
    selisih = car[1].car_possition(x) - car[0].car_possition(x)
    selisih1 = car[2].car_possition(x) - car[3].car_possition(x)
    car[0].car_move()
    if selisih < 25:
        car[0].car_speed(2,0)
    elif selisih > 40 and selisih < 100:
        car[0].car_speed(3,0)
        car[0].car_move()
    elif selisih == 100:
        car[0].car_speed(2,0)
        car[0].car_move()
    elif selisih > 150 and selisih < 280:
        car[0].car_speed(3,0)
        car[0].car_move()
    elif selisih == 280:
        car[0].car_speed(2,0)
        car[0].car_move()
    elif selisih > 280:
        car[0].car_speed(4,0)
    car[1].car_move()

    car[2].car_move()
    if selisih1 > -20:
        car[3].car_speed(-1,0)
    elif selisih1 < -45 and selisih1 > -70:
        car[3].car_speed(-2,0)
        car[3].car_move()
    elif selisih1 == -70:
        car[3].car_speed(-3,0)
        car[3].car_move()
    elif selisih1 < -80 and selisih1 > -120:
        car[3].car_speed(-4,0)
        car[3].car_move()
    elif selisih1 < -150:
        car[3].car_speed(-4,0)
    car[3].car_move()

    car[4].car_move()
    selisih2 = car[3].car_possition(x) - car[0].car_possition(x)
    selisih3 = car[3].car_possition(x) - car[5].car_possition(x)
    if selisih2 > 75:
        car[3].car_speed(5,0)
        car[5].car_speed(3,0)
        car[5].car_move()
    elif selisih2 > 90:
        car[3].car_speed(3,0)
        car[3].car_move()
    if selisih3 == 60:
        car[5].car_speed(2,0)
        car[5].car_move()
    elif selisih3 >= 220:
        car[5].car_speed(2,0)
    car[5].car_move()

    selisih4 = car[6].car_possition(x) - car[3].car_possition(x)
    car[6].car_move()
    if selisih4 < -55 and selisih4 > -70:
        car[6].car_speed(-4,0)
        car[7].car_speed(-5,0)
        car[7].car_move()
    elif selisih4 < -70 and selisih4 > -75:
        car[6].car_speed(-4,0)
        car[7].car_speed(-4,0)
    elif selisih4 < -75:
        car[7].car_speed(-3,0)
    car[7].car_move()

    car[8].car_move()
    car[9].car_move()

    return car

def car_movement_reset(car, x):
    for i in range(5):
        if x == 320*i:
            car[0].car_reset()
            car[0].car_new_possition(-40, 155, -20, 170, fill='blue')
            car[0].car_speed(5,0)

    for i in range(5):
        if x == 300*i:
            car[1].car_reset()
            car[1].car_new_possition(-20, 155, 0, 170, fill = 'green')

    for i in range(5):
        if x == 320*i:
            car[2].car_reset()
            car[2].car_new_possition(1000, 180, 1020, 195, fill = 'red')
        
    for i in range(5):
        if x == 330*i:
            car[3].car_reset()
            car[3].car_new_possition(1040, 180, 1060, 195, fill = 'cyan')

    for i in range(5):
        if x == 350*i:
            car[6].car_reset()
            car[6].car_new_possition(1120, 180, 1140, 195, fill = 'yellow')

    for i in range(5):
        if x == 380*i:
            car[7].car_reset()
            car[7].car_new_possition(1200, 180, 1220, 195, fill = 'pink')

    for i in range(5):
        if x == 370*i:
            car[4].car_reset()
            car[4].car_new_possition(-120, 155, -100, 170, fill = 'orange')

    for i in range(5):
        if x == 400*i:
            car[5].car_reset()
            car[5].car_new_possition(-160, 155, -140, 170, fill = 'maroon')

    for i in range(5):
        if x == 410*i:
            car[8].car_reset()
            car[8].car_new_possition(-300, 155, -280, 170, fill = 'gold')

    for i in range(5):
        if x == 400*i:
            car[9].car_reset()
            car[9].car_new_possition(1320, 180, 1340, 195, fill = 'purple')

    return car