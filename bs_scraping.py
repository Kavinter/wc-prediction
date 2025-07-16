from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

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


def get_matches(year):
    if year == 2022:
        web = "https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup"
    else:
        web = f"https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup"

    response = requests.get(web)
    content = response.text
    soup = bs(content, "lxml")

    matches = soup.find_all("div", class_="footballbox")

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find("th", class_="fhome").get_text().strip())
        score.append(match.find("th", class_="fscore").get_text().strip())
        away.append(match.find("th", class_="faway").get_text().strip())

    dict_football = {"home": home, "score": score, "away": away}
    df_football = pd.DataFrame(dict_football)
    df_football["year"] = year
    return df_football


print(get_matches(1990))

fifa = []
for year in years:
    fifa.append(get_matches(year))


df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv("fifa_worldcup_data.csv", index=False)

df_fixture = get_matches(2022)
df_fixture.to_csv("fifa_worldcup_fixture.csv", index=False)
