---
quang.bui.2@city.ac.uk: N3061/INM430 Principles of Data Science
---

# Exercises (DIY) - Part 0
To make sure that you get an intial exposure to the Jupyter Notebook, transfer the code from Week-1's exercise and build a notebook that implements the Part-1 of the solutions of Practical session of Week-01.

# DIY Exercises - 2 : Missing values
For the exercises here, we use a modified version of data from a Kaggle competition. Kaggle is a platform for predictive modelling and analytics competitions on which companies and researchers post their data and statisticians and data miners from all over the world compete to produce the best models. The original data and description is here but for our exercise most of the information here is a bit out of scope.

Load the slightly modified Titanic survival data  into a pandas data frame.
Find the counts of missing values in each column
Compute the mean and other descriptive statistics and note these down, you can use this function
Replace the missing values in "Age" and "Fare" columns with 0 values, and visualise in a scatterplot
Replace the missing values in "Age" and "Fare" columns with the mean of each column, and visualise in a scatterplot
Reflect on the differences you see in these plots.

# DIY Exercises - 3 : Data Transformations
Here we test a couple of data distributions and observe how they change the data.
Download the csv data file from WHO on Tuberculosis (from Week01)  . Information on the data can be found on WHO's web page.
You may need to replace missing values before you start.
Choose a number of columns with different shapes, for instance, "e_prev_100k_hi" is right skewed and visualise on an histogram
Apply a log transformation on the data. Numpy has a log function. and visualise. Observe the changes
Choose the numerical columns and map all the columns to [0,1] interval
Now you can compare the means of each column.

## The file was jupyter notebook file (not github - friendly) therefore, to view this, the user should download the file