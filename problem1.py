"""
----------------------------------------------------------
Name:    problem1.py
Purpose: Write a program that asks the user to enter three           values and then determines whether the triangle             created is a right-angled triangle or not.

Author:  Hosey.K

Created: date in 12/02/2021
----------------------------------------------------------
"""

# Get the information
side_1 = int(input("Enter the length of side 1: "))
side_2 = int(input("Enter the length of side 2: "))
side_3 = int(input("Enter the length of side 3: "))

# Get the sqaured values of the lengths 
squared_1 = side_1**2
squared_2 = side_2**2
squared_3 = side_3**2

# Compute Results
if (squared_1 + squared_2 == squared_3) or (squared_2 + squared_3 == squared_1) or (squared_1 + squared_3 == squared_2):
  print("The triangle with side lengths " + str(side_1) + ", " + str(side_2) + ", and " + str(side_3) + " form a right-angled traingle.")
else:
  print("The triangle with side lengths " + str(side_1) + ", " + str(side_2) + ", and " + str(side_3) + " do not form a right-angled traingle.")