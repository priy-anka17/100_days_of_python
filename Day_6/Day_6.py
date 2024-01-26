## Day: 6 Function

## def my_function
# Do this
# then do this 
# Finally do this 
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()


def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

number_of_hurdles = 6
while number_of_hurdles > 0:
    my_turn()
    number_of_hurdles -=1
    print(number_of_hurdles)

#While Loop
## While something_is true:
#Do this 
#Then do this 
# Then do this 



while at_goal() != True:
    my_turn()

## Another way to use while 

while at_goal() != True:
    my_turn()


## Hurdle 3 

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
def my_turn():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        my_turn()
    else:
        move()
 
    
    
    ## Hurdle 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
def my_turn():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        my_turn()
    else:
        move()


##Maze 

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        

