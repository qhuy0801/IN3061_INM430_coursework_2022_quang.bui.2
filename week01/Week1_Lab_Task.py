## BASIC PYTHON COMMAND
import pandas as pd
import math

df = pd.read_csv("TB_burden_countries_2014-09-29.csv", header = 0)

# Count the number of rows
row_count = 1 # Since we skipped the header
for index, row in df.iterrows():
    row_count += 1
print("The number of rows: ", row_count)


# Get the average of column "e_prev_num_lo"
sum_e_prev_num_lo = 0
for index, row in df.iterrows():
    if math.isnan(row["e_prev_num_lo"]) == False:
        sum_e_prev_num_lo += row["e_prev_num_lo"]
avg_e_prev_num_lo = sum_e_prev_num_lo / (row_count - 1)
print(avg_e_prev_num_lo)

# Get the average of column "e_prev_num_lo" for year = 1990
sum_e_prev_num_lo_1990 = 0
row_count_1990 = 0
for index, row in df.iterrows():
    if row["year"] == 1990 and math.isnan(row["e_prev_num_lo"]) == False:
        sum_e_prev_num_lo_1990 += row["e_prev_num_lo"]
        row_count_1990 += 1
avg_e_prev_num_lo_1990 = sum_e_prev_num_lo_1990 / row_count_1990
print(avg_e_prev_num_lo_1990)

# Get the average of column "e_prev_num_lo" for year = 2011
sum_e_prev_num_lo_2011 = 0
row_count_2011 = 0
for index, row in df.iterrows():
    if row["year"] == 2011 and math.isnan(row["e_prev_num_lo"]) == False:
        sum_e_prev_num_lo_2011 += row["e_prev_num_lo"]
        row_count_2011 += 1
avg_e_prev_num_lo_2011 = sum_e_prev_num_lo_2011 / row_count_2011
print(avg_e_prev_num_lo_2011)

#%%
## NUMPY BASICS
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(5, 16)

b = np.linspace(0, 23, 7, endpoint= True)

c = np.random.uniform(-1, 1, 30)

plt.hist(c, bins = 25)

d = np.random.rand(10)
e = np.random.rand(10)
dist = np.sqrt(np.sum(np.square(d-e)))
print("Euclidean distance: ", dist)
