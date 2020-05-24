from gateway import *
from algorithms import *

rows = int(input("Rows: "))
cols = int(input("Columns: "))
passengers = int(input("Passengers: "))
seats = [[0 for i in range(cols)] for j in range(rows)]

capacity_percentage = round(passengers / (rows * cols), 2)
print("Capacity percentage: " + str(capacity_percentage))

seats = [[0 for i in range(cols)] for j in range(rows)]

if (cols == 1):
	single(rows, cols, passengers, seats, capacity_percentage)
elif (cols == 2):
	double(rows, cols, passengers, seats, capacity_percentage)
elif (cols == 3):
	triple(rows, cols, passengers, seats, capacity_percentage)
elif (rows < passengers):
	breakdown(rows, cols, passengers, seats, capacity_percentage)
else:
	triple(rows, cols, passengers, seats, capacity_percentage)

for x in seats:
	print(x)







