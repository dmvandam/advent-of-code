import numpy as np

# load data
depths = np.loadtxt('data/puzzle1.txt')

# part 1
differences = depths[1:] - depths[:-1]
numMeasurements = np.sum(differences > 0)

print('part 1 - %i' % numMeasurements)

# part 2
differencesSmoothed = np.convolve(differences, np.ones(3), mode='valid')
numMeasurementsSmoothed = np.sum(differencesSmoothed > 0)

print('part 2 - %i' % numMeasurementsSmoothed)
