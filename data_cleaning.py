import pandas as pd

df_worldcup_data = pd.read_csv("fifa_worldcup_data.csv")
df_missing_data = pd.read_csv("fifa_missing_data.csv")

df_worldcup_data = pd.concat([df_worldcup_data, df_missing_data], ignore_index=True)
df_worldcup_data.drop_duplicates(inplace=True)
df_worldcup_data.sort_values("year", inplace=True)

## deleting the game because it is a walkover
index_delete = df_worldcup_data[
    df_worldcup_data["home"].str.contains("Sweden")
    & df_worldcup_data["away"].str.contains("Austria")
].index

df_worldcup_data = df_worldcup_data.drop(index_delete)


## replacing the matches which scores ends with (a.e.t) or any other possible non number of hyphen
df_worldcup_data["score"] = df_worldcup_data["score"].str.replace(
    "[^\d–]", "", regex=True
)

## splitting the score between home goals and away goals in each match
df_worldcup_data[["HomeGoals", "AwayGoals"]] = df_worldcup_data["score"].str.split(
    "–", expand=True
)

df_worldcup_data = df_worldcup_data.drop("score", axis=1)

df_worldcup_data = df_worldcup_data.rename(
    columns={"home": "HomeTeam", "away": "AwayTeam", "year": "Year"}
)

df_worldcup_data = df_worldcup_data.astype(
    {"Year": int, "HomeGoals": int, "AwayGoals": int}
)

df_worldcup_data["TotalGoals"] = df_worldcup_data[["HomeGoals", "AwayGoals"]].sum(
    axis=1
)

df_worldcup_data.to_csv("cleaned_df_worldcup_data.csv", index=False)

years = [
    1930,
    1934,
    1938,
    1950,
    1954,
    1958,
    1962,
    1966,
    1970,
    1974,
    1978,
    1982,
    1986,
    1990,
    1994,
    1998,
    2002,
    2006,
    2010,
    2014,
    2018,
]

for year in years:
    print(year, len(df_worldcup_data[df_worldcup_data["Year"] == year]))
