import numpy as np

def problem1(filename):
    '''
    Many diagnostics are recorded in single lines of bytes. By processing
    the byte code it is possible to determine the power consumption. The
    gamma rate is the most common bit in every column, and the epsilon rate
    is the least common bit in every column of the report.

    Parameters
    ----------
    filename : str
        This is the name of the file that contains the data
    '''
    # load the data
    bitCodes = np.loadtxt(filename, dtype=str)

    numCodes = len(bitCodes)
    numBytes = len(bitCodes[0])

    # set bit arrays
    gamma = ''
    epsilon = ''

    # loop through position
    for i in range(numBytes):
        print(i)
        # define ones and zeros
        ones = 0
        zeros = 0

        # loop through codes
        for bitCode in bitCodes:
            bit = bitCode[i]
            if bit == '0':
                zeros += 1
            else:
                ones += 1
        print('ones: %i' % ones)
        print('zeros: %i' % zeros)
        print('numCodes: %i' % numCodes)
        print('missing: %i' % (numCodes - ones - zeros))
        # add most common bit to gamma and least common to epsilon
        if ones > zeros:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
        print('gamma: %s' % gamma)
        print('epsilon: %s' % epsilon)

    # convert bytes to integers
    gammaVal = int(gamma, 2)
    epsilonVal = int(epsilon, 2)

    # get power consumption and display
    powerConsumption = gammaVal * epsilonVal

    print('problem1 answer: %i' % powerConsumption)

    return None

def problem2(filename):
    '''
    

    Parameters
    ----------
    filename : str
        This is the name of the file that contains the data
    '''
    return None

def main():
    '''
    This is the main function to solve this puzzle
    '''
    # define data file
    filename = 'data/puzzle3.txt'

    # solve the puzzle
    problem1(filename)
    problem2(filename)
    problem1(filename)
    problem2(filename)

    return None

if __name__ == "__main__":
    main()

