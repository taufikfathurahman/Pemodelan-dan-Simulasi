from tkinter import *
import time
from car_model import *

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

car = make_car_model(my_car)
car = set_car_speed(car)

for x in range(1000):
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

  #perulangan untuk kembali ke posisi awal
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

  screen.update()

root.mainloop() 