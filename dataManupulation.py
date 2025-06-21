import pandas as pd

data = {
    "Name": ["Fahim", "Saad", "Nur"],
    "Age": [27, 28, 29],
    "Salary": [25000, 50000, 60000],
    "Performance": [88, 89, 95]
}

df = pd.DataFrame(data)
# print(df)

# selecting single coloumn (will return series)
# print(df['Name'])
# for employeeName in df['Name']:
#     print(employeeName)

# selecting multiple coloumns (will return data frame)
# selectedData = df[["Name", "Age"]]
# print(selectedData)

# single condition
highSalary = df[df['Salary'] > 30000]
print("Employee with high Salary: ")
print(highSalary)

highSalaryAndPerformance = df[(df['Salary'] > 30000) & (df['Performance'] > 90)]
print("Employee with high Salary & Perfromance: ")
print(highSalaryAndPerformance)

highSalaryOrPerformance = df[(df['Salary'] > 30000) | (df['Performance'] > 90)]
print("Employee with high Salary or Perfromance: ")
print(highSalaryOrPerformance)