from algorithms import *

def single(rows, cols, passengers, seats, capacity_percentage):
	A_dynamic(rows, cols, passengers, seats)

def double(rows, cols, passengers, seats, capacity_percentage):
	if (0 <= capacity_percentage <= .25):
		A_dynamic(rows, cols, passengers, seats)
	if (.25 < capacity_percentage <= .5):
		B_dynamic(rows, cols, passengers, seats)
	if (.5 < capacity_percentage <= .66):
		C_dynamic(rows, cols, passengers, seats)
	if (.66 < capacity_percentage <= .8):
		D_dynamic(rows, cols, passengers, seats)
	if (.8 < capacity_percentage <= 1):
		print("under development")

def triple(rows, cols, passengers, seats, capacity_percentage):
	if (0 <= capacity_percentage <= .15):
		A_dynamic(rows, cols, passengers, seats)
	if (.15 < capacity_percentage <= .33):
		B_dynamic(rows, cols, passengers, seats)
	if (.33 < capacity_percentage <= .50):
		C_dynamic(rows, cols, passengers, seats)
	if (.50 < capacity_percentage <= .8):
		D_dynamic(rows, cols, passengers, seats)
	if (.8 < capacity_percentage <= 1):
		print("under development")

def breakdown(rows, cols, passengers, seats, capacity_percentage):
	divider = (cols // 2)
	remainder = (passengers % divider)
	grouping = (passengers // divider)
	counter = 0
	if (cols % 2 == 0):
		for i in range(0, divider):
			local_seats = [[0 for i in range(2)] for j in range(rows)]
			double(rows, 2, grouping, local_seats, capacity_percentage)
			join_array(seats, local_seats, counter, rows, 2)
			counter += 1
	else:
		for i in range(0, divider-1):
			local_seats = [[0 for i in range(2)] for j in range(rows)]
			double(rows, 2, grouping, local_seats, capacity_percentage)
			join_array(seats, local_seats, counter, rows, 2)
			counter += 1
		local_seats = [[0 for i in range(3)] for j in range(rows)]
		triple(rows, 3, grouping + remainder, local_seats, capacity_percentage)
		join_array(seats, local_seats, counter, rows, 3)
		counter += 1

def join_array(seats, local_seats, offset, rows, cols):
	if (cols % 2) == 0:
		index = offset*(cols)
	else:
		index = offset*(cols-1)
	for curr_row in range(0, rows):
		for curr_col in range(0, cols):
			if local_seats[curr_row][curr_col] == 1:
				seats[curr_row][curr_col + index] = 1

