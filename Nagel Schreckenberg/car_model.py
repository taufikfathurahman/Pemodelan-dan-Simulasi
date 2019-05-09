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