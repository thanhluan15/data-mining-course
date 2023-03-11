
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
print(min(gdp_bq["GDP"]))

# Max
print(gdp_bq["GDP"].max())

# Mean (Average)
print(gdp_bq["GDP"].mean())

# Median
print(gdp_bq["GDP"].median())








# print("aaa")

# name = "aaaa";

# print(name)

# anime = "Blood"

# arr = [{"anime": "Date a Live"}, name]

# print(type(arr))

# min(3,4,5,2,3)

# print(min(3,4,5,2,3,1,9))