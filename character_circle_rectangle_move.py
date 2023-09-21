#Agile Software Development 에자일 코딩
from pico2d import *
import math

open_canvas()

glass = load_image('grass.png')
character = load_image('character.png')

def move_circle(): 
    
    #일단 그림을 그리자
    cx, cy, r = 800 // 2, 600 // 2, 200
    
    for degree in range(0,360,5):
        x = cx + r * math.cos(math.radians(degree))
        y = cy + r * math.sin(math.radians(degree))
        clear_canvas_now()
        glass.draw_now(400,30)
        character.draw_now(x, y)
        delay(0.01)

def move_rectangle():
    for x in range(50,750+1,10):
        clear_canvas_now()
        glass.draw_now(400,30)
        character.draw_now(x, 90)
        delay(0.01)    
    
    pass



while True:
    # move_circle()
    move_rectangle()
    break
    
close_canvas()

