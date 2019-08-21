import pandas as pd #imports pandas to use
url = "https://archive.ics.uci.edu/m1/machine-learningdatabases/autos/imports-85.data"

df = pd.read_csv(url, header = None)
#no header is in the CSV data file se we specify header = none

df.head(n)
headers = ["symboling","normalized-loses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horepower","peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers #replaces the numbers as the correct headers we want

path = #file path and file name you want to write to
#df.to_csv(path) #saves path as csv file
