import numpy as np

# load the data

# part 1
def problem1(filename):
    '''
    You're in a submarine and you have a lot of instructions to navigate.
    Forward X --> increase your horizontal position by X
    Up X --> decreases your depth position by X
    Down X --> increases your depth coordinate by X

    Parameters
    ----------
    filename : str
        the name of the file containing the navigation instructions
    '''
    # extract data
    directions = np.loadtxt(filename, usecols=0, dtype=str)
    values = np.loadtxt(filename, usecols=1)

    # define starting point
    x = 0
    y = 0

    # go through instructions
    for direction, value in zip(directions, values):
        if direction == 'forward':
            x += value
        elif direction == 'up':
            y -= value
        elif direction == 'down':
            y += value
        else:
            print('error encountered')
    
    # answer
    answer = x * y
    
    # print to terminal
    print('problem1 answer: %i' % answer)       

    return None

def problem2(filename):
    '''
    You're in a submarine with a navigation plan. After the set of
    instructions you want to know the product of your horizontal and
    depth coordinates. We need to track the aim of the submarine.
    Down X --> increase aim by X
    Up X --> decreases aim by X
    Forward X --> horizontal coordinate increases by X, 
                  depth coordinate increases by Aim times X

    Parameters
    ----------
    filename : str
        the name of the file containing the navigation instructions
    '''
    # extract data
    directions = np.loadtxt(filename, usecols=0, dtype=str)
    values = np.loadtxt(filename, usecols=1)

    # define starting point
    x = 0
    y = 0
    aim = 0

    # go through instructions
    for direction, value in zip(directions, values):
        if direction == 'forward':
            x += value
            y += aim * value
        elif direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value
        else:
            print('error encountered')
    
    # answer
    answer = x * y
    
    # print to terminal
    print('problem2 answer: %i' % answer)   

    return None    

def main():
    '''
    Main program that runs problem 1 and 2 and sets the filename
    '''
    # set filename
    filename = 'data/puzzle2.txt'

    # solve problems
    problem1(filename)
    problem2(filename)

    return None
    
if __name__ == "__main__":
    main()
