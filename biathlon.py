from random import randint

def splash():
    print( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print( "          Biathlon                    ")
    print( "      a hit or miss game              ")
    print( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

splash()

open   = 0
closed = 1
a = open
b = closed
def is_open(value):
    if value == open:
        return True
    else:
        return False
    
def is_closed(value):
    if value == closed:
        return True
    elif value == open:
        return False

def new_targets():
    return [open, open, open, open, open]

def close_target(targets, position):
    if targets[position] == open:
        targets[position] = closed
def points(targets):
    n = 0
    for i in targets:
        if is_closed(i):
            n +=1
    return n

def target_to_string(targets):
    a = []    
    for n in targets:
        if is_closed(n):
            a.append('*')
        else:    
            a.append('0')
    return ' '.join(a)

def view_targets():
    print("0 1 2 3 4")
    print(			 )
    print(target_to_string(ts))

def random_hit():
    s = randint(0,1)
    if s == 1:
        return True
    elif s == 0:
        return False

def shoot(targets, position):
    if is_open(targets[position]):
        if random_hit() == True:
            close_target(targets, position)
            print("Hit on open target")
        elif random_hit() == False:
            print("Miss")
    elif is_closed(targets[position]):
        if random_hit() == True:
            print ("Hit on closed target")
        else:
            print("Miss")
