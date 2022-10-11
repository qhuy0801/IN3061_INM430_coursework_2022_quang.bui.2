---
quang.bui.2@city.ac.uk: N3061/INM430 Principles of Data Science
---

# DIY Exercises Part-1: Some elementary Python tasks
Count the number of rows in the csv file you've chosen.
Pick one of the columns with numeric data and calculate the average value using a loop (not a library function such as avg(), we'll come to those soon). One candidate is the column with the name "e_prev_num_lo" which is "Estimated prevalence of TB (all forms), low bound" according to the dictionary here.
Hint-1: Do not forget to skip the first line here which is the header line with column names. You can make use of the next(f) statement to do this.

Hint-2: In the loop above, row is basically a list. So row[0] will give you the values along the first column.

Hint-3: to convert the string to a number, use the float() function (which converts to a floating point number)

Hint-4: some of the values in the table are blank, so converting to a number will cause an error. Try to detect spaces using if or use try: and except: to ignore these.

Now, repeat step-2 above but this time find the averages for years 1990 and 2011. Have you observed any difference?

# Exercises (DIY) - Part 2
Create an array of int ranging from 5-15

Create an array containing 7 evenly spaced numbers between 0 and 23

Numpy has several routines for generating artificial data following a particular structure. Check this page for different types. And generate an artificial numpy array with values between -1 and 1 that follow a uniform data distribution.

Visualise the array in an histogram in matplotlib.

Create two random numpy arrays with 10 elements. Find the Euclidean distance between the arrays using arithmetic operators, hint: numpy has a sqrt function

