import pandas as pd

data = {
    "Name": ['Faim', 'Hossain', 'Alif'],
    "Age": [10,20,30],
    "City": ["Dhaka", "Rajshahi", "Khulna"]
}
df = pd.DataFrame(data)
df.to_json("output.json", index=False)

data2 = [
    {
        "Name": "Fahim Hossain",
        "Age": 27
    },
    {
        "Name": "Jobaida Yasmin",
        "Age": 26
    }
]
df = pd.DataFrame(data2)
df.to_json("output.json", index=False, orient='records', indent=2)

# print(df)
# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
# df.to_json("output.json", index=False)