import os
import pandas as pd

# get all of the excels and store them into file_list
path = "/Users/kacpermocarski/Desktop/New_Excels"
file_list = os.listdir(path)

df = pd.DataFrame()

df_list = []

for xls in file_list:
    read_file = pd.read_excel(path + "/" + xls)
    read_file.to_csv("data.csv", index=None, header=True)
    # df = df.append(pd.read_csv("data.csv", header=5))
    df = pd.read_csv("data.csv", header=5, low_memory=False)
    df_list.append(df)

df = pd.concat(df_list)

df.to_csv(path+"/combined_data.csv", index=False)
