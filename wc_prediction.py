import pandas as pd
import pickle
from scipy.stats import poisson
from typing import Dict

dict_table: Dict[str, pd.DataFrame] = pickle.load(open("dict_table.pkl", "rb"))
df_worldcup_data = pd.read_csv("cleaned_df_worldcup_data.csv")
df_fixtures = pd.read_csv("fifa_worldcup_fixture.csv")

df_home = df_worldcup_data[["HomeTeam", "HomeGoals", "AwayGoals"]]
df_away = df_worldcup_data[["AwayTeam", "HomeGoals", "AwayGoals"]]

df_home = df_home.rename(
    columns={
        "HomeTeam": "Team",
        "HomeGoals": "GoalsScored",
        "AwayGoals": "GoalsConceded",
    }
)
df_away = df_away.rename(
    columns={
        "AwayTeam": "Team",
        "HomeGoals": "GoalsConceded",
        "AwayGoals": "GoalsScored",
    }
)

df_team_strength = (
    pd.concat([df_home, df_away], ignore_index=True).groupby("Team").mean()
)


def predict_points(home, away):
    if home in df_team_strength.index and away in df_team_strength.index:
        lambda_home = (
            df_team_strength.at[home, "GoalsScored"]
            * df_team_strength.at[away, "GoalsConceded"]
        )
        lambda_away = (
            df_team_strength.at[away, "GoalsScored"]
            * df_team_strength.at[home, "GoalsConceded"]
        )
        prob_home = 0
        prob_away = 0
        prob_draw = 0
        for x in range(0, 11):
            for y in range(0, 11):
                prob = poisson.pmf(x, lambda_home) * poisson.pmf(y, lambda_away)
                if x > y:
                    prob_home += prob
                elif x < y:
                    prob_away += prob
                else:
                    prob_draw += prob

        home_points = 3 * prob_home + prob_draw
        away_points = 3 * prob_away + prob_draw
        return (home_points, away_points)
    else:
        return (0, 0)


df_fixtures_group = df_fixtures[:48].copy()
df_fixtures_knockout = df_fixtures[48:56].copy()
df_fixtures_quarter = df_fixtures[56:60].copy()
df_fixtures_semi = df_fixtures[60:62].copy()
df_fixtures_final = df_fixtures[62:].copy()


for group in dict_table:

    teamsInGroup = dict_table[group]["Team"].values
    df_fixtures_group_6 = df_fixtures_group[
        df_fixtures_group["home"].isin(teamsInGroup)
    ]
    for index, row in df_fixtures_group_6.iterrows():
        home = row["home"]
        away = row["away"]
        home_points, away_points = predict_points(home, away)
        dict_table[group].loc[dict_table[group]["Team"] == home, "Pts"] += home_points
        dict_table[group].loc[dict_table[group]["Team"] == away, "Pts"] += away_points

    dict_table[group] = (
        dict_table[group].sort_values("Pts", ascending=False).reset_index()
    )
    dict_table[group] = dict_table[group][["Team", "Pts"]]
    dict_table[group] = dict_table[group].round(0)

for group in dict_table:
    winner_group = dict_table[group].iloc[0, 0]
    runnerup_group = dict_table[group].iloc[1, 0]

    df_fixtures_knockout = df_fixtures_knockout.replace(
        {f"Winners {group}": winner_group, f"Runners-up {group}": runnerup_group}
    )
    df_fixtures_knockout["winner"] = "?"


def get_winner(df_updated_fixtures):
    for index, row in df_updated_fixtures.iterrows():
        home = str(row["home"])
        away = str(row["away"])
        home_points, away_points = predict_points(home, away)
        if home_points > away_points:
            winner = home
        else:
            winner = away
        df_updated_fixtures.loc[index, "winner"] = winner

    return df_updated_fixtures


df_fixtures_knockout = get_winner(df_fixtures_knockout)


def table_update(df_fixture_round_1, df_fixture_round_2):
    for index, row in df_fixture_round_1.iterrows():
        winner = df_fixture_round_1.loc[index, "winner"]
        match = df_fixture_round_1.loc[index, "score"]
        df_fixture_round_2 = df_fixture_round_2.replace({f"Winners {match}": winner})
    df_fixture_round_2["winner"] = "?"

    return df_fixture_round_2


df_fixtures_quarter = table_update(df_fixtures_knockout, df_fixtures_quarter)

df_fixtures_quarter = get_winner(df_fixtures_quarter)

df_fixtures_semi = table_update(df_fixtures_quarter, df_fixtures_semi)

df_fixtures_semi = get_winner(df_fixtures_semi)

df_fixtures_final = table_update(df_fixtures_semi, df_fixtures_final)

for index, row in df_fixtures_semi.iterrows():
    home = str(row["home"])
    away = str(row["away"])
    winner = row["winner"]
    match = row["score"]

    if home == winner:
        df_fixtures_final = df_fixtures_final.replace({f"Losers {match}": away})
    else:
        df_fixtures_final = df_fixtures_final.replace({f"Losers {match}": home})

df_fixtures_final = get_winner(df_fixtures_final)

print(df_fixtures_final)
