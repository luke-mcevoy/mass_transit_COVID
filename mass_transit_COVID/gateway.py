# Title: 	gateway.py
# Author: 	Luke McEvoy
# Created: 	May 18, 2020
# Summary:	Optimized space between passengers on mass transit

from algorithms import *

# Function when row count is multiple of one
def single(rows, cols, passengers, seats, capacity_percentage):
	A_dynamic(rows, cols, passengers, seats)

	
# Function when row count is multiple of two
def double(rows, cols, passengers, seats, capacity_percentage):
	# Passenger capacity threshold [0% - 25%)
	if (0 <= capacity_percentage <= .25):
		A_dynamic(rows, cols, passengers, seats)
		
	# Passenger capacity threshold (25% -> 50%]
	if (.25 < capacity_percentage <= .5):
		B_dynamic(rows, cols, passengers, seats)
		
	# Passenger capacity threshold (50% -> 66%]
	if (.5 < capacity_percentage <= .66):
		C_dynamic(rows, cols, passengers, seats)
		
	# Passenger capacity threshold (66% -> 80%]
	if (.66 < capacity_percentage <= .8):
		D_dynamic(rows, cols, passengers, seats)
	
	# Passenger capacity threshold (80% -> 100%]
	if (.8 < capacity_percentage <= 1):
		print("under development")
		
		
# Function when row count is multiple of three
def triple(rows, cols, passengers, seats, capacity_percentage):
	# Passenger capacity threshold (0% -> 15%]
	if (0 <= capacity_percentage <= .15):
		A_dynamic(rows, cols, passengers, seats)
		
	# Passenger capacity threshold (15% -> 33%]
	if (.15 < capacity_percentage <= .33):
		B_dynamic(rows, cols, passengers, seats)
		
	# Passenger capacity threshold (33% -> 50%]
	if (.33 < capacity_percentage <= .50):
		C_dynamic(rows, cols, passengers, seats)
		
	# Passenger capacity threshold (50% -> 80%]
	if (.50 < capacity_percentage <= .8):
		D_dynamic(rows, cols, passengers, seats)
		
	# Passenger capacity threshold (80% -> 100%]
	if (.8 < capacity_percentage <= 1):
		print("under development")

		
# Divides up the work into 2D array blocks.
#	Example. 10 x 6 are would be divided into three 10 x 2 blocks.
# This allows the algorithm to be consistent with patterns.
def breakdown(rows, cols, passengers, seats, capacity_percentage):
	# divider represents how many blocks will be segmented
	divider = (cols // 2)
	# remainder shows if there is an odd number
	remainder = (passengers % divider)
	# grouping represents passengers to be allocated in each segmented block
	grouping = (passengers // divider)
	# counter repsents
	counter = 0
	# Even amount of columns
	if (cols % 2 == 0):
		for i in range(0, divider):
			# Create a local 2D array to do seating algorithm on
			local_seats = [[0 for i in range(2)] for j in range(rows)]
			double(rows, 2, grouping, local_seats, capacity_percentage)
			# Merge local 2D array called local_seats with global 2D array called seats
			join_array(seats, local_seats, counter, rows, 2)
			# Increment counter variable
			counter += 1
	# Odd amount of columns
	else:
		for i in range(0, divider-1):
			# Create a local 2D array to do seating algorithm on
			local_seats = [[0 for i in range(2)] for j in range(rows)]
			double(rows, 2, grouping, local_seats, capacity_percentage)
			# Merge local 2D array called local_seats with global 2D array called seats
			join_array(seats, local_seats, counter, rows, 2)
			# Increment counter variable
			counter += 1
		# Create a local 2D array to do seating algorithm on
		local_seats = [[0 for i in range(3)] for j in range(rows)]
		triple(rows, 3, grouping + remainder, local_seats, capacity_percentage)
		# Merge local 2D array called local_seats with global 2D array called seats
		join_array(seats, local_seats, counter, rows, 3)
		# Increment counter variable
		counter += 1

# Merges the local_seats 2D array with the global seats 2D array
def join_array(seats, local_seats, offset, rows, cols):
	if (cols % 2) == 0:
		index = offset*(cols)
	else:
		index = offset*(cols-1)
	for curr_row in range(0, rows):
		for curr_col in range(0, cols):
			if local_seats[curr_row][curr_col] == 1:
				seats[curr_row][curr_col + index] = 1

