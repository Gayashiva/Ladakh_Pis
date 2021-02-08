import os
import numpy as np
import sys
import glob
import pandas as pd
import re
import datetime as dt
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from Setup.config import site, dir

def remove_empty_columns(df, threshold=0.9):
    column_mask = hobo.isnull().mean(axis=0) > threshold
    return df.loc[:, column_mask]

# set working directory
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
name = site(path)
os.chdir(dir+ "/hobo/")
# find all csv files in the folder
# use glob pattern matching -> extension = 'csv'
# save result in list -> all_filenames
extension = "csv"
all_filenames = [i for i in glob.glob("*.{}".format(extension))]

reobj = re.compile("\A"+ name + "_hobo")
file = [f for f in all_filenames if reobj.match(f)][0]
hobo = pd.read_csv(file)
print(file)

print(hobo.head())
if name == 'kullum':
    hobo = hobo.fillna(0)
    i=1
    for column in hobo.columns[1:4]:
        hobo[column] +=hobo[hobo.columns[i+3]]
        print(column, hobo.columns[i+3])
        i += 1
hobo = hobo.drop(hobo.columns[3:], axis=1)
hobo.columns = ["Datetime", "Air_Temp", "RH"]
hobo["Datetime"] = pd.to_datetime(hobo["Datetime"], format="%y-%m-%d %H:%M:%S")
hobo["Datetime"] = hobo["Datetime"].dt.strftime("%Y-%m-%d %H:%M")
print(hobo.head())

hobo.to_csv(path + "/Data/hobo.csv", index=False)
