#Agile Software Development 에자일 코딩
from pico2d import *

open_canvas()

glass = load_image('grass.png')
character = load_image('character.png')

def move_circle(): 
    print('CIRCLE')

    #일단 그림을 그리자
    clear_canvas_now()
    glass.draw_now(400,30)
    character.draw_now(400,90)
    delay(1)
    
    pass

def move_rectangle():
    print('rectangle')
    pass



while True:
    move_circle()
    move_rectangle()
    break
    
close_canvas()

