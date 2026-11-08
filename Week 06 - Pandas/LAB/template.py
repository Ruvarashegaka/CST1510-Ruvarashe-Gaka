"""
RECORD CHECK  -  my version
===========================

Name  :  Ruvarashe Gaka
Lane  :  IT      (delete two)
Date  : 30/10/2026 

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

#reading the values put in the folder using exact path

df = pd.read_csv(r"C:\Users\Admin\Documents\CST1510-Ruvarashe-Gaka\Week 06 - Pandas\LAB\Ruvas_file.csv")  
#addition of 2 other columns into the Datafram
df["percent"] = df["used_gb"] / df["Total_gb"] * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK")

print("=" * 55)
print(df)
print("=" * 55)
warning = df[(df["percent"] >= 90)]
print(warning)
print("=" * 55)
#saving a new file with the updated records to a new csv file
df.to_csv("updated_records.csv", index=False)
#making a bar chart to show the status counts and saving it as a png file
import matplotlib.pyplot as plt
df["status"].value_counts().plot(kind="bar")
plt.savefig("status_counts.png")
plt.show()
# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
