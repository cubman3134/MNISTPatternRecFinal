
import sys
import os
import random
import numpy as np

def get_n_train_samples( n, total ):

	# Make set of indexes to grab n random samples	
	n_samples = set()

	for i in range( 0, n ):
		
		x = random.randint( 0, total )
		while x in n_samples:
			x = random.randint( 0, total-1 )
		
		n_samples.add( x )
		
	
	# Use set to grab associated samples from training data
	train_file = open( "mnist_tr_data.txt", "r" )

	X_list = list()
	y_list = list()
	i = 0

	rows = 28
	cols = 28

	for line in train_file:

		if i in n_samples:

			line = line.split()
			sample = line[0:(rows*cols)]
			label = line[-1]
			
			X_list.append( sample )
			y_list.append( label )

		i += 1

	train_file.close()

	X = np.asarray( X_list, dtype=np.float64 )  
	y = np.asarray( y_list, dtype=np.float64 )  

	# Return X, y as numpy arrays and n_samples as set
	# for getting test data
	return X, y, n_samples

def get_n_test_samples( n, total, used ):

	# Make set of indexes to grab n random samples	
	n_samples = set()

	for i in range( 0, n ):
		
		x = random.randint( 0, total )
		while x in n_samples or x in used:
			x = random.randint( 0, total-1 )
		
		n_samples.add( x )
		
	# Use set to grab associated samples from training data
	train_file = open( "mnist_te_data.txt", "r" )

	X_list = list()
	y_list = list()
	i = 0

	rows = 28
	cols = 28

	for line in train_file:

		if i in n_samples:

			line = line.split()
			sample = line[0:(rows*cols)]
			label = line[-1]
			
			X_list.append( sample )
			y_list.append( label )

		i += 1

	train_file.close()

	X = np.asarray( X_list, dtype=np.float64 )  
	y = np.asarray( y_list, dtype=np.float64 )  

	# Return X, y as numpy arrays and n_samples as set
	# for getting test data
	return X, y, n_samples
if __name__ == "__main__":

	X, y, n_samples = get_n_train_samples( 10, 60000 )

	print( X )
	print( y )
