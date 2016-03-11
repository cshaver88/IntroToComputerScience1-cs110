from gasp import *          # import everything from the gasp library


def draw_house(x,y):
    Box((x+20,y+20), 100, 100)     # the house
    Box((x+55, y+20), 30, 50)       # the door
    Box((x+40, y+80), 20, 20)       # the left window
    Box((x+80, y+80), 20, 20)       # the right window
    Line((x+20, y+120), (x+70, y+160))  # the left roof
    Line((x+70, y+160), (x+120, y+120)) # the right roof

begin_graphics()            # open the graphics canvas

draw_house(100,100)
draw_house(100,10)
draw_house(30,60)
draw_house(50,70)
draw_house(1,7)


update_when('key_pressed')  # keep the canvas open until a key is pressed
end_graphics()              # close the canvas (which would happen
                            # anyway, since the script ends here, but it
                            # is better to be explicit).
