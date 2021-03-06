import pandas as pd

csv = 'LACS_print_lit.csv'

df = pd.read_csv(csv)

df['Series'] = df['Call Number'].astype(str).str[0:2]

# Organize by series then by sublibrary, then tally it up
df2 = df.groupby(['Series', 'Sublibrary'])['Sublibrary'].count()

print(df2)
