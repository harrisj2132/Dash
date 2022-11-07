import pandas as pd

df=pd.read_excel(r'C:\Users\venkat\Downloads\Sample - Superstore.xls')

df_cat=df.groupby('Category',as_index=False)['Sales'].sum()

df_subcat=df.groupby('Sub-Category',as_index=False)['Sales'].sum()

df_prod=df.groupby('Product Name',as_index=False)['Sales'].sum()