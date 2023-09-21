from pico2d import *

open_canvas()

glass = load_image('grass.png')
character = load_image('character.png')

def move_circle(): #pass : 아무것도 안하고 넘김
    print('CIRCLE')
    pass

def move_rectangle():
    print('rectangle')
    pass
    

while True:
    move_circle()
    move_rectangle()

    
close_canvas()

