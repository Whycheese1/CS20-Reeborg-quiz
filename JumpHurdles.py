from library import*

def jump_hurdle():
    while wall_in_front(): 
        turn_left()
    if wall_on_right():
        while wall_on_right():
            move()
        if not wall_on_right():
                turn_right()
                move()
                turn_right()
                while front_is_clear():
                    move()
                    

think(90)
if wall_in_front():
    jump_hurdle()
    turn_left()
while front_is_clear(): #reeborg walking until he meets a wall
    move()
    if wall_in_front():
        jump_hurdle()
        turn_left()
    if at_goal(): # if reeborg is at the goal he'll stop, finishing his "mission" or something
        done()    #im not good at commenting my codes, sorry :(
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_around():
    turn_left()
    turn_left()
    
    
def turn_right():
    repeat 3:
        turn_left()
        

#def jump_hurdle():
#    if front_is_clear():
#        while front_is_clear():
#            move()
#        else wall_in_front():
#            turn_left()
#            move()
#            turn_right()
#            move()
#            turn_right()
#            move()
#            turn_left()

#the previvous code was for the older stages in reeborg in CS20
