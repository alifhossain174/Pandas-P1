import pandas as pd
print(pd.__version__)

# read data from a CSV file
# df = pd.read_csv("Applied_Jobs.csv", encoding="utf-8")
# df = pd.read_csv("Applied_Jobs.csv", encoding="latin1")
# dataFrame = pd.read_excel("Applied_Jobs.xlsx") # need to install openpyxl

dataFrame2 = pd.read_json("users.json")
print(dataFrame2)