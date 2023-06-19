import pandas as pd
import numpy as np

d1= pd.read_csv('melb_data.csv')
print(d1)

df = pd.DataFrame(d1)

print(df)

# drop all rows with any NaN and NaT values
df1 = df.dropna()
print(df1)