import pandas as pd

df = pd.read_csv('sample.csv')
df_clean = df.drop_duplicates()
df_clean.to_csv('sample_clean.csv', index=False)
print("Duplicates removed and saved as 'sample_clean.csv'.")
