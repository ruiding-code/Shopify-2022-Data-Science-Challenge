import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

# find the average order value of sneakers

# reading in data from csv as pandas dataframe
data = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv", encoding= 'unicode_escape')

# checking first 3 rows to see if we read in the csv file properly
#display(raw_data.iloc[:3, :])

# viewing first 6 rows of order_amount
#display(raw_data.loc[:5, ["order_amount"]])


# Checking min, max, mean, median, mode order_amount values

print(data.order_amount.max())
print(data.order_amount.min())
print(data.order_amount.mean())
print(data.order_amount.median())
print(data.order_amount.mode())
print(data.order_amount.quantile(0.99))

# we get max = 704 000 and min = 90
# mean = 3145.128, median = 284, mode = 153

# Seems like some orders are huge (2000 items), maybe we can filter out the invalid data by obtaining avg unit price per sneaker for each order

data["average_amount_per_item"] = (data["order_amount"])/(data["total_items"])
display(data.iloc[:3, :])

print(data.average_amount_per_item.max()) # 25725$ seems way too much for the unit price of a sneaker...
print(data.average_amount_per_item.mean())

upper = data.average_amount_per_item.quantile(0.999) # use this as upper bound to remove invalid values
print(upper)

data = data[data["average_amount_per_item"] < upper]

print(data.average_amount_per_item.max()) # 352 is a more reasonable value for the unit price of a sneaker

data = data[data["order_amount"] < 704000] # remove valid, but outlier value

print(data.order_amount.max()) # 1760$
print(data.order_amount.min()) # 90$
print(data.order_amount.mean()) # 302.58$
print(data.order_amount.median()) # 284$
print(data.order_amount.mode()) # 153$

# should take the median or mode?




order_amounts = np.sort(np.array(data["order_amount"]))
plt.hist(order_amounts)
plt.show() # data is right skewed

# we should use the median since it is less influenced by extremely large values
# which is 284$
