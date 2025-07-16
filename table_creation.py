import pandas as pd
import pickle
from string import ascii_uppercase as alphabet

all_tables = pd.read_html(
    "https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup"
)

dict_table = {}

for l, i in zip(alphabet, range(12, 68, 7)):
    df = all_tables[i]
    df = df.rename(columns={df.columns[1]: "Team"})
    df.pop(df.columns[10])
    dict_table[f"Group {l}"] = df

##print(dict_table.keys())
##print(dict_table['Group A'])

with open("dict_table.pkl", "wb") as output:
    pickle.dump(dict_table, output)
