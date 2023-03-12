import numpy as np
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.stats import kurtosis

comRpTimes = pd.read_excel("D:\ComputerRepairTimes.xlsx")

print(comRpTimes)

# Count
print(len(comRpTimes))

#Min
print(comRpTimes["Repair Time (Days)"].min())

#Max
print(comRpTimes["Repair Time (Days)"].max())

#Mean (Average)
# print(comRpTimes["Repair Time (Days)"].mean())
print(st.mean(comRpTimes["Repair Time (Days)"]))

#Median
# print(comRpTimes["Repair Time (Days)"].median())
print(st.median(comRpTimes["Repair Time (Days)"]))

#Mode
print(st.mode(comRpTimes["Repair Time (Days)"]))

#Quantile
print(st.quantiles(comRpTimes["Repair Time (Days)"]))

#Range
print((comRpTimes["Repair Time (Days)"].max() - comRpTimes["Repair Time (Days)"].min()))

#Variance
print(st.variance(comRpTimes["Repair Time (Days)"]))

# Standard Deviation
print(st.stdev(comRpTimes["Repair Time (Days)"]))

#Coefficient of variation = Standard Deviation / Mean
print(st.stdev(comRpTimes["Repair Time (Days)"]) / st.mean(comRpTimes["Repair Time (Days)"]))

#Skewness
print(skew(comRpTimes["Repair Time (Days)"]))

#Kurtosis
print(kurtosis(comRpTimes["Repair Time (Days)"]))

### Using Visualization

#Histogram
histogram  = plt.hist(comRpTimes["Repair Time (Days)"])
plt.show()

#Box Plot
boxplot = plt.boxplot(comRpTimes["Repair Time (Days)"])
plt.show()

