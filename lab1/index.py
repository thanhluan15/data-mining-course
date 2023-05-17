
import numpy as np
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.stats import kurtosis

gdp_bq = pd.read_excel("D:\GDP_2000_2022.xlsx")
gdp_bq

# print(gdp_bq)

# Count
print(len(gdp_bq))

# Min
print("Min: ", gdp_bq["GDP"].min())

# Max
print("Max: ", gdp_bq["GDP"].max())

# Mean (Average)
print("Mean: ", gdp_bq["GDP"].mean())

# Median
print("Median: ", gdp_bq["GDP"].median())

# Variance
print("Variance: ", gdp_bq["GDP"].var())

# Range
print("Range: ", gdp_bq["GDP"].max()-gdp_bq["GDP"].min())

# Mode
print("Mode: ", gdp_bq["GDP"].mode())

# Quantile

 
# print(gdp_bq["GDP"][3])


# print("aaa")

# name = "aaaa";

# print(name)

# anime = "Blood"

# arr = [{"anime": "Date a Live"}, name]

# print(type(arr))

# min(3,4,5,2,3)

# print(min(3,4,5,2,3,1,9))
