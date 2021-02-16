"""
----------------------------------------------------------
Name:    problem2.py
Purpose: Write a program that determines whether the user can go on a summer vacation.

Author:  Hosey.K

Created: date in 12/02/2021
----------------------------------------------------------
"""

# Get the information
grade = float(input("Enter your averaged (%): "))
earnings = float(input("Enter the the earnings: "))

# Compute Results
if grade >= 80 and earnings >= 500:
  print("Congratulations! You get to go on a trip to Europe for your summer vacation.")
elif grade >= 80 and earnings <= 500:
  print("Congratulations! You get to go on a trip to California for your summer vacation.")
else:
  print("Sorry! You do not get a summer vacation. There's always next time!")