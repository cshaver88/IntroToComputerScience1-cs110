from gasp import *          # import everything from the gasp library


def draw_house(x,y):
    Box((x+20,y+20), 100, 100, True, color.BLUE)     # the house
    Box((x+55, y+20), 30, 50, True, color.GREEN)       # the door
    Box((x+40, y+80), 20, 20, True, color.YELLOW)       # the left window
    Box((x+80, y+80), 20, 20, True, color.YELLOW)       # the right window
    Polygon([(x+20,y+120),(x+70,y+160),(x+120,y+120)], True, color.RED) # the roof

begin_graphics(800, 600, "Houses at Night", color.BLACK)            # open the graphics canvas


draw_house(0,0)
draw_house(320,0)
draw_house(620,0)
draw_house(150,200)
draw_house(450,200)
draw_house(320,400)

update_when('key_pressed')  # keep the canvas open until a key is pressed
end_graphics()              # close the canvas (which would happen
                            # anyway, since the script ends here, but it
                            # is better to be explicit).
