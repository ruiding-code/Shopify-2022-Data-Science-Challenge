import pandas as pd
from IPython.display import display

# find the average order value of sneakers

# reading in data from csv as pandas dataframe
raw_data = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv", encoding= 'unicode_escape')

# checking first 3 rows to see if we read in the csv file properly
display(raw_data.iloc[:3,:])