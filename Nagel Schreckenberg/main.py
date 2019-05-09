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
    car = car_movement(car, x)
    car = car_movement_reset(car, x)
    screen.update()

root.mainloop() 