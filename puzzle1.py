import numpy as np

def problem1(filename):
    '''
    You're in a submarine and want to find how often you are increasing
    your depth based on a navigation plan
    
    Parameters
    ----------
    filename : str
        this is a file that contains the depth measurements
    '''
    # load data
    depths = np.loadtxt(filename)

    # determine the differences in the measurements
    differences = depths[1:] - depths[:-1]
    
    # determine the number of measurements that increase the depth
    numMeasurements = np.sum(differences > 0)

    print('problem1 answer: %i' % numMeasurements)

    return None

def problem2(filename):
    '''
    You're in a submarine and want to find how often you are increasing
    your depth based on a navigation plan. The results are too noisy so
    add the measurements before and after the current measurement to get
    more accurate

    Parameters
    ----------
    filename : str
        this is a file that contains the depth measurements
    '''
    # load data
    depths = np.loadtxt(filename)

    # determine the differences in the measurements
    differences = depths[1:] - depths[:-1]
    
    # smooth with a window function
    smoothedDifferences = np.convolve(differences, np.ones(3), mode='valid')
    
    # determine the number of measurements that increase the depth
    numMeasurements = np.sum(smoothedDifferences > 0)

    print('problem2 answer: %i' % numMeasurements)

    return None

def main():
    '''
    Main program that solves the first puzzle
    '''
    # define data file
    filename = 'data/puzzle1.txt'

    # solve puzzle
    problem1(filename)
    problem2(filename)

    return None

if __name__ == "__main__":
    main()

