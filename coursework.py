import pandas as pd

df = pd.read_csv("dataset/laptops.csv")

print(df.sort_values(by="Company"))