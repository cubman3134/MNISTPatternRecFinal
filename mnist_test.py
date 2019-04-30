

import sys
import os

data_file = open( "mnist_te_data.txt", "r" )

rows = 28
cols = 28

test_num = 5
tests = 0
for line in data_file:

	line = line.split()
	
	for i in range( 0, rows ):  
		row = list()
		for j in range( 0, cols ):
			row.append( line[ (i*cols) + j ] )
		print( row )

	print( "label: {}".format( line[784] ) )

	tests += 1
	if tests == test_num:
		break;

data_file.close()
