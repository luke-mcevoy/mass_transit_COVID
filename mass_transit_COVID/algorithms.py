# Title: 	Mass transit passenger placement - COVID
# Author: 	Luke McEvoy
# Created: 	May 18, 2020
# Summary:	Optimized space between passengers on mass transit

import math

def everyone_seated(seats, seated, passengers):
	if seated == passengers:
		return True
	return False

def A_dynamic(rows, cols, passengers, seats):
	extra_rows = (rows - passengers)
	seated = 0
	tmp = 0
	for curr_row in range(0, rows):
		curr_col = (seated % 2) * (cols - 1)
		if seats[curr_row + tmp][curr_col] == 0:
			seats[curr_row + tmp][curr_col] = 1
			seated += 1
			if extra_rows > 0:
				tmp += (extra_rows // passengers) + 1
				extra_rows -= 1
			if (everyone_seated(seats, seated, passengers)):
				break

def B_dynamic(rows, cols, passengers, seats):
	extra_rows = (rows - passengers)
	seated = 0
	tmp = 0
	for curr_row in range(0, rows):
		curr_col = (seated % 2) * (cols - 1)
		if seats[curr_row + tmp][curr_col] == 0:
			seats[curr_row + tmp][curr_col] = 1
			seated += 1
			if extra_rows > 0:
				tmp += 1
				extra_rows -= 1
			if (everyone_seated(seats, seated, passengers)):
				break

def C_dynamic(rows, cols, passengers, seats):
	extra_rows = rows - (passengers * (2/3)) // 1
	seated = 0
	tmp = 0
	for curr_row in range(0, rows):
		# current row is even
		if (curr_row % 2) == 0:
			# the rightmost seat is open
			if seats[curr_row + tmp][cols-1] == 0:
				seats[curr_row + tmp][cols-1] = 1
				seated += 1
				if (everyone_seated(seats, seated, passengers)):
					break
			# the leftmost seat is open
			if seats[curr_row + tmp][0] == 0:
				seats[curr_row + tmp][0] = 1
				seated += 1
				if (everyone_seated(seats, seated, passengers)):
					break
		# current row is odd
		else:
			# the middle seat
			if seats[curr_row + tmp][cols//2] == 0:
				seats[curr_row + tmp][cols//2] = 1
				seated += 1
				if (everyone_seated(seats, seated, passengers)):
					break

def D_dynamic(rows, cols, passengers, seats):
	extra_rows = rows - math.ceil(passengers//2)
	seated = 0
	tmp = 0
	for curr_row in range(0, rows):
		if seats[curr_row + tmp][0] == 0:
			seats[curr_row + tmp][0] = 1
			seated += 1
			if (everyone_seated(seats, seated, passengers)):
				break
		if seats[curr_row + tmp][cols-1] == 0:
			seats[curr_row + tmp][cols-1] = 1
			seated += 1
			if (everyone_seated(seats, seated, passengers)):
				break
		if extra_rows > 1:
				tmp += 1
				extra_rows -= 1



