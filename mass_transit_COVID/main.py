# Title: 	main.py
# Author: 	Luke McEvoy
# Created: 	May 18, 2020
# Summary:	Optimized space between passengers on mass transit

from gateway import *
from algorithms import *

# User inputs
rows = int(input("Rows: "))
cols = int(input("Columns: "))
passengers = int(input("Passengers: "))

# Declaration of global 2D array seats. Used as seating chart.
seats = [[0 for i in range(cols)] for j in range(rows)]

capacity_percentage = round(passengers / (rows * cols), 2)
print("Capacity percentage: " + str(capacity_percentage))

# If statements to appropriate function in regards to column sizes.
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

# Output final seating chart
for x in seats:
	print(x)







