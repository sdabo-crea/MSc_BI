#pip install pandas numpy matplotlib seaborn streamlit
#Importing libraries to the local environment and create abbrevations for easier usage
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
url = "https://drive.google.com/file/d/19NrHoe7TzNrwzQg5AkfxtJFDaVe7-F0Y/view?usp=share_link"(url, "uber-raw-data-apr14.csv", quiet=False)
# Reading the csv file into a pandas dataframe
path = "uber-raw-data-apr14.csv"
df = pd.read_csv(path, delimiter = ',')
df.head
df.tail
df['Date/Time'] = df['Date/Time'].map(pd.to_datetime)
def get_dom(dt):
    return dt.day #.day is an attribute
df['day'] = df['Date/Time'].map(get_dom)
def get_weekday(dt):
    return dt.weekday() #.weekday() is a method
df['weekday'] = df['Date/Time'].map(get_weekday)
def get_hour(dt):
    return dt.hour
def get_hour(dt):
    return dt.hour
hist = df["day"].plot.hist(bins = 30, rwidth = 0.8, range=(0.5,30.5), title = "Frequency by DoM - Uber - April 2014")
plt.xlabel('Days of the month')
#binsint or sequence or str, default: rcParams["hist.bins"] (default: 10)
#If bins is an integer, it defines the number of equal-width bins in the range.
#If bins is a sequence, it defines the bin edges, including the left edge of the first bin and the right edge of the last bin; in this case, bins may be unequally spaced.
def count_rows(rows):
    return len(rows)
by_date = df.groupby('day').apply(count_rows)
by_date
plt.title('Line plot - Uber - April 2014')
plt.xlabel('Days of the month')
plt.ylabel('Frequency')
plt.plot(by_date)
plt.figure(figsize = (25, 15))
plt.bar(range(1, 31), by_date.sort_values())
plt.xticks(range(1, 31), by_date.sort_values().index)
plt.xlabel(('Date of the month'), fontsize=20)
plt.ylabel(('Frequency'), fontsize=20)
plt.title(('Frequency by DoM - Uber - April 2014'), fontsize=20)
plt.figure(figsize = (25, 15))
plt.bar(range(1, 31), by_date.sort_values())
plt.xticks(range(1, 31), by_date.sort_values().index)
plt.xlabel(('Date of the month'), fontsize=20)
plt.ylabel(('Frequency'), fontsize=20)
plt.title(('Frequency by DoM - Uber - April 2014'), fontsize=20)
#plt.figure(figsize = (15, 15))
plt.hist(df.weekday, bins = 7, rwidth = 0.8, range = (-.5, 6.5))
plt.xlabel('Days of the week')
plt.ylabel('Frequency')
plt.title('Frequency by Weekdays - Uber - April 2014')
plt.hist(df.weekday, bins = 7, rwidth = 0.8, range = (-.5, 6.5))
plt.xlabel('Day of the week')
plt.ylabel('Frequency')
plt.title('Frequency by Weekdays - Uber - April 2014')
plt.xticks(np.arange(7), 'Tue Wed Thu Fri Sat Sun Mon'.split())
plt.show()
df2 = df.groupby(['weekday', 'hour']).apply(count_rows).unstack()
df2.head()
#Pandas Unstack is a function that pivots the level of the indexed columns in a stacked dataframe. A stacked dataframe is usually a result of an aggregated groupby function in pandas. Stack() sets the columns to a new level of hierarchy whereas Unstack() pivots the indexed column.
heatmap = sns.heatmap(df2, linewidths = .5)
#Annoted heatmap
plt.title('Heatmap by Hour and weekdays - Uber - April 2014',fontsize=15)
heatmap.set_yticklabels(('Mar Mer Jeu Ven Sam Dim Lun').split(), rotation='horizontal')
#Lat :
plt.hist(df['Lat'], bins = 100, range = (40.5, 41), color = 'r',alpha = 0.5, label = 'Latitude')
plt.xlabel('Latitude')
plt.ylabel('Frequency')
plt.title('Lattitude - Uber - April 2014')
plt.show()
#Lon :
plt.hist(df['Lon'], bins = 100, range = (-74.1, -73.9), color = 'g', alpha = 0.5, label = 'Longitude')
plt.xlabel('Longitude')
plt.ylabel('Frequency')
plt.title('Longitude - Uber - April 2014')
plt.show()
plt.figure(figsize=(10, 10), dpi=100)
plt.title('Longitude and Latitude distribution - Uber - April 2014',fontsize=15)
plt.hist(df['Lon'], bins = 100, range = (-74.1, -73.9), color = 'g', alpha = 0.5, label = 'Longitude')
plt.legend(loc = 'best')
plt.twiny()
plt.hist(df['Lat'], bins = 100, range = (40.5, 41), color = 'r',alpha = 0.5, label = 'Latitude')
plt.legend(loc = 'upper left')
plt.show()
#Map
plt.figure(figsize=(15, 15), dpi=100)
plt.title('Scatter plot - Uber - April 2014')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.scatter(df['Lat'],df['Lon'],s=0.8,alpha=0.4) #Without list also shows the same plot
plt.ylim(-74.1, -73.8)
plt.xlim(40.7, 40.9)
#Yellow Map
plt.figure(figsize=(15, 15), dpi=100)
plt.title('Scatter plot - Uber - April 2014')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.scatter(df['Lat'],df['Lon'],s=0.8,alpha=0.4) #Without list also shows the same plot
plt.ylim(-74.1, -73.8)
plt.xlim(40.7, 40.9)