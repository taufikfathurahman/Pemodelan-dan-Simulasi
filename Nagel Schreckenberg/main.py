from tkinter import *
import time
import car_model

root = Tk()
root.title("Nagel Schreckenberg")
screen = Canvas(root, width=1080, height=720, bg='#96ec5f')
screen.pack()

data_road = [
    (0,300,500,300),
    (1080,300,500,300),
    (0,500,500,500),
    (1080,500,500,500)
    ]
    
for my_tup in data_road:
    screen.create_line(my_tup, width=5)
    road_color = [(0,302,1080,498)]

for my_tup in road_color:
    screen.create_rectangle(my_tup, fill="grey")
    road_line = [(0,400,1080,400)]

    for my_tup in road_line:
        screen.create_line(my_tup, width=10, fill="white")

class my_car(object):

    def __init__(self, sisi1, sisi2, sisi3, sisi4, fill='white'):
        self.car = screen.create_rectangle(sisi1, sisi2, sisi3, sisi4, fill=fill)
        self.speed = (0, 0)

    def car_move(self):
        screen.move(self.car, self.speed[0], self.speed[1])
    
    def car_speed(self, x, y):
        self.speed = x, y
    
    def car_possition(self, pos):
        curr_possition = self.speed[0] * pos
        return curr_possition
    
    def car_reset(self):
        screen.delete(self.car)

    def car_new_possition(self, sisi1, sisi2, sisi3, sisi4, fill):
        self.car = screen.create_rectangle(sisi1, sisi2, sisi3, sisi4, fill=fill)

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

car1.car_speed(3,0)
car2.car_speed(5,0)
car3.car_speed(-5,0)
car4.car_speed(-3,0)
car5.car_speed(4,0)
car6.car_speed(3,0)
car7.car_speed(-4,0)
car8.car_speed(-3,0)
car9.car_speed(5,0)
car10.car_speed(-4,0)

for x in range(1000):
  time.sleep(0.005)

  selisih = car2.car_possition(x) - car1.car_possition(x)
  selisih1 = car3.car_possition(x) - car4.car_possition(x)
  car1.car_move()
  if selisih < 25:
    car1.car_speed(2,0)
  elif selisih > 40 and selisih < 100:
    car1.car_speed(3,0)
    car1.car_move()
  elif selisih == 100:
    car1.car_speed(2,0)
    car1.car_move()
  elif selisih > 150 and selisih < 280:
    car1.car_speed(3,0)
    car1.car_move()
  elif selisih == 280:
    car1.car_speed(2,0)
    car1.car_move()
  elif selisih > 280:
    car1.car_speed(4,0)
  car2.car_move()

  car3.car_move()
  if selisih1 > -20:
    car4.car_speed(-1,0)
  elif selisih1 < -45 and selisih1 > -70:
    car4.car_speed(-2,0)
    car4.car_move()
  elif selisih1 == -70:
    car4.car_speed(-3,0)
    car4.car_move()
  elif selisih1 < -80 and selisih1 > -120:
    car4.car_speed(-4,0)
    car4.car_move()
  elif selisih1 < -150:
    car4.car_speed(-4,0)
  car4.car_move()

  car5.car_move()
  selisih2 = car5.car_possition(x) - car1.car_possition(x)
  selisih3 = car5.car_possition(x) - car6.car_possition(x)
  if selisih2 > 75:
    car5.car_speed(5,0)
    car6.car_speed(3,0)
    car6.car_move()
  elif selisih2 > 90:
    car5.car_speed(3,0)
    car5.car_move()
  if selisih3 == 60:
    car6.car_speed(2,0)
    car6.car_move()
  elif selisih3 >= 220:
    car6.car_speed(2,0)
  car6.car_move()

  selisih4 = car7.car_possition(x) - car4.car_possition(x)
  car7.car_move()
  if selisih4 < -55 and selisih4 > -70:
    car7.car_speed(-4,0)
    car8.car_speed(-5,0)
    car8.car_move()
  elif selisih4 < -70 and selisih4 > -75:
    car7.car_speed(-4,0)
    car8.car_speed(-4,0)
  elif selisih4 < -75:
    car8.car_speed(-3,0)
  car8.car_move()

  car9.car_move()
  car10.car_move()

  #perulangan untuk kembali ke posisi awal
  for i in range(5):
    if x == 320*i:
      car1.car_reset()
      car1.car_new_possition(-40, 155, -20, 170, fill='blue')
      car1.car_speed(5,0)

  for i in range(5):
    if x == 300*i:
      car2.car_reset()
      car2.car_new_possition(-20, 155, 0, 170, fill = 'green')

  for i in range(5):
    if x == 320*i:
      car3.car_reset()
      car3.car_new_possition(1000, 180, 1020, 195, fill = 'red')
      
  for i in range(5):
    if x == 330*i:
      car4.car_reset()
      car4.car_new_possition(1040, 180, 1060, 195, fill = 'cyan')

  for i in range(5):
    if x == 350*i:
      car7.car_reset()
      car7.car_new_possition(1120, 180, 1140, 195, fill = 'yellow')

  for i in range(5):
    if x == 380*i:
      car8.car_reset()
      car8.car_new_possition(1200, 180, 1220, 195, fill = 'pink')

  for i in range(5):
    if x == 370*i:
      car5.car_reset()
      car5.car_new_possition(-120, 155, -100, 170, fill = 'orange')

  for i in range(5):
    if x == 400*i:
      car6.car_reset()
      car6.car_new_possition(-160, 155, -140, 170, fill = 'maroon')

  for i in range(5):
    if x == 410*i:
      car9.car_reset()
      car9.car_new_possition(-300, 155, -280, 170, fill = 'gold')

  for i in range(5):
    if x == 400*i:
      car10.car_reset()
      car10.car_new_possition(1320, 180, 1340, 195, fill = 'purple')

  screen.update()

root.mainloop() 