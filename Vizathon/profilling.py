import pandas as pd
df=pd.read_excel('First.xlsx')
print(df)

from pandas_profiling import ProfileReport
profile=ProfileReport(df)
profile.to_file(output_file="First.html")